# -*- coding: utf-8 -*-
"""
============================================================
        小说朗读器  —— 多音色有声小说阅读软件
============================================================
功能：
  * 打开 TXT/MD 小说（自动识别编码 UTF-8/GBK 等）
  * 自由选择音色（晓晓 / 云希 / 云健 / 台湾/香港/方言……）
  * 语速、音量实时调节
  * 断句分块 + 后台预生成（双缓冲）流畅播放，支持暂停/继续/停止
  * 自动记忆阅读进度，下次打开同一文件续读
  * 一键导出整本小说为 MP3

依赖：pip install edge-tts pygame chardet
说明：edge-tts 调用微软在线语音服务，需要联网。
============================================================
"""
import asyncio
import collections
import os
import queue
import re
import sys
import tempfile
import threading
import time
import uuid
import json

import edge_tts
import pygame
import chardet

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# ---------------------------------------------------------------------------
# 内置常用中文音色表（离线备用；启动时会联网刷新完整列表）
# ---------------------------------------------------------------------------
STATIC_VOICES = [
    ("zh-CN-XiaoxiaoNeural", "晓晓 · 温柔女声（推荐）"),
    ("zh-CN-XiaoyiNeural",   "晓伊 · 活泼女声"),
    ("zh-CN-YunxiNeural",    "云希 · 阳光男声"),
    ("zh-CN-YunjianNeural",  "云健 · 成熟男声"),
    ("zh-CN-YunyangNeural",  "云扬 · 沉稳男声"),
    ("zh-CN-YunxiaNeural",   "云夏 · 男声"),
    ("zh-CN-liaoning-XiaobeiNeural", "晓北 · 东北话女声"),
    ("zh-CN-shaanxi-XiaoniNeural",   "晓妮 · 陕西话女声"),
    ("zh-CN-guangxi-YunqiNeural",    "云奇 · 广西话男声"),
    ("zh-CN-henan-YundengNeural",    "云登 · 河南话男声"),
    ("zh-TW-HsiaoChenNeural", "曉晨 · 台湾女声"),
    ("zh-TW-HsiaoYuNeural",   "曉雨 · 台湾女声"),
    ("zh-TW-YunJheNeural",    "雲哲 · 台湾男声"),
    ("zh-HK-HiuGaaiNeural",   "曉佳 · 香港女声"),
    ("zh-HK-HiuMaanNeural",   "曉曼 · 香港女声"),
    ("zh-HK-WanLungNeural",   "雲龍 · 香港男声"),
]
VOICE_LOOKUP = {name: vid for vid, name in STATIC_VOICES}

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reader_config.json")

# ---------------------------------------------------------------------------
# 文本分块：按句号/感叹/问号等断句，避免机械切分导致断句别扭
# ---------------------------------------------------------------------------
SENT_END = re.compile(r"(?<=[。！？；…!?;])|(?<=\n)")
CLAUSE   = re.compile(r"(?<=[，、,：:])")

def split_into_chunks(text, max_chars=250):
    """把整本小说切成适合 TTS 的片段（默认 ≤250 字）。"""
    chunks = []

    def push(s):
        if s.strip():
            chunks.append(s)

    def hard_split(s):
        """兜底：把无标点的超长文本强制按 max_chars 切分。"""
        while len(s) > max_chars:
            push(s[:max_chars])
            s = s[max_chars:]
        push(s)

    # 先按换行分段落
    for para in re.split(r"\n+", text):
        para = para.strip()
        if not para:
            continue
        # 再按句号等强分隔符断句
        sentences = re.split(SENT_END, para)
        cur = ""
        for sent in sentences:
            if not sent.strip():
                continue
            if len(sent) > max_chars:
                # 长句按逗号二次拆分
                for clause in re.split(CLAUSE, sent):
                    if len(clause) > max_chars:
                        # 仍超长（无标点），先落盘当前 cur，再硬切
                        if cur:
                            push(cur)
                            cur = ""
                        hard_split(clause)
                    else:
                        if len(cur) + len(clause) > max_chars and cur:
                            push(cur)
                            cur = ""
                        cur += clause
            else:
                if len(cur) + len(sent) > max_chars and cur:
                    push(cur)
                    cur = ""
                cur += sent
        if cur:
            push(cur)
    return chunks

# ---------------------------------------------------------------------------
# 语音合成工作线程：后台逐个把文本合成为 mp3
# ---------------------------------------------------------------------------
class SynthWorker(threading.Thread):
    def __init__(self, tmpdir):
        super().__init__(daemon=True)
        self.tmpdir = tmpdir
        self.cond = threading.Condition()
        self.jobs = collections.deque()
        self.results = {}          # idx -> mp3 path (None 表示失败)
        self._stop = threading.Event()

    def run(self):
        while not self._stop.is_set():
            with self.cond:
                while not self.jobs and not self._stop.is_set():
                    self.cond.wait(0.2)
                if self._stop.is_set():
                    break
                idx, text, voice, rate = self.jobs.popleft()
            try:
                path = self._synth_one(text, voice, rate)
            except Exception:
                path = None
            with self.cond:
                self.results[idx] = path
                self.cond.notify_all()

    @staticmethod
    def _synth_one(text, voice, rate, tries=4):
        """合成一段 mp3。网络抖动时自动重试（edge-tts 在线服务偶发连接重置）。"""
        path = os.path.join(tempfile.gettempdir(), f"tts_{uuid.uuid4().hex}.mp3")
        last_err = None
        for attempt in range(1, tries + 1):
            try:
                loop = asyncio.new_event_loop()
                try:
                    async def do():
                        c = edge_tts.Communicate(text, voice, rate=rate)
                        await c.save(path)
                    loop.run_until_complete(do())
                finally:
                    loop.close()
                if os.path.getsize(path) > 0:
                    return path
                last_err = RuntimeError("生成文件为空")
            except Exception as e:
                last_err = e
                if attempt < tries:
                    time.sleep(1.5 * attempt)
        # 全部失败：清理残留文件
        try:
            os.remove(path)
        except OSError:
            pass
        raise last_err

    def request(self, idx, text, voice, rate):
        with self.cond:
            if idx in self.results:
                return
            self.jobs.append((idx, text, voice, rate))
            self.cond.notify()

    def get(self, idx, timeout=None):
        with self.cond:
            self.cond.wait_for(lambda: idx in self.results, timeout=timeout)
            return self.results[idx]

    def stop(self):
        self._stop.set()
        with self.cond:
            self.cond.notify_all()


# ---------------------------------------------------------------------------
# 主程序
# ---------------------------------------------------------------------------
class NovelReaderApp:
    def __init__(self, root):
        self.root = root
        root.title("小说朗读器 · 多音色有声阅读")
        root.geometry("860x620")
        root.minsize(720, 520)

        # ---- 状态 ----
        self.chunks = []
        self.file_path = None
        self.index = 0
        self.reading = False
        self.requested = set()
        self.stop_flag = threading.Event()
        self.pause_flag = threading.Event()
        self.ui_queue = queue.Queue()
        self.worker = None
        self.tmpdir = tempfile.mkdtemp(prefix="novel_tts_")
        self.config = self._load_config()

        # 恢复上次设置
        self.voice = self.config.get("voice", "zh-CN-XiaoxiaoNeural")
        self.rate_val = int(self.config.get("rate", 0))
        self.volume = float(self.config.get("volume", 0.8))

        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()

        self._build_ui()
        self._apply_settings()
        self._poll_ui_queue()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # 后台刷新完整音色列表（失败则保留内置列表）
        threading.Thread(target=self._refresh_voices, daemon=True).start()

    # ================== 界面 ==================
    def _build_ui(self):
        pad = {"padx": 8, "pady": 4}

        # 文件选择
        frm_file = ttk.LabelFrame(self.root, text=" 小说文件 ")
        frm_file.pack(fill="x", **pad)
        self.var_file = tk.StringVar()
        ent = ttk.Entry(frm_file, textvariable=self.var_file)
        ent.pack(side="left", fill="x", expand=True, padx=6, pady=6)
        ttk.Button(frm_file, text="打开小说…", command=self.open_file).pack(side="left", padx=6)
        ttk.Button(frm_file, text="从头读", command=self.restart).pack(side="left", padx=6)

        # 音色
        frm_voice = ttk.LabelFrame(self.root, text=" 音色 ")
        frm_voice.pack(fill="x", **pad)
        self.var_voice = tk.StringVar(value=VOICE_LOOKUP.get(self.voice, STATIC_VOICES[0][1]))
        self.cmb_voice = ttk.Combobox(frm_voice, textvariable=self.var_voice,
                                      values=[n for _, n in STATIC_VOICES], width=34, state="readonly")
        self.cmb_voice.pack(side="left", padx=6, pady=6)
        ttk.Button(frm_voice, text="试听", command=self.preview_voice).pack(side="left", padx=6)
        ttk.Button(frm_voice, text="刷新音色列表", command=self.refresh_voices_manual).pack(side="left", padx=6)

        # 语速 / 音量
        frm_slider = ttk.Frame(self.root)
        frm_slider.pack(fill="x", **pad)
        ttk.Label(frm_slider, text="语速").pack(side="left", padx=(8, 4))
        self.rate_var = tk.DoubleVar(value=self.rate_val)
        self.scl_rate = ttk.Scale(frm_slider, from_=-50, to=50, orient="horizontal",
                                  variable=self.rate_var, command=self.on_rate_change)
        self.scl_rate.pack(side="left", fill="x", expand=True)
        self.lbl_rate = ttk.Label(frm_slider, text="+0%", width=6)
        self.lbl_rate.pack(side="left", padx=4)

        ttk.Label(frm_slider, text="音量").pack(side="left", padx=(12, 4))
        self.vol_var = tk.DoubleVar(value=int(self.volume * 100))
        self.scl_vol = ttk.Scale(frm_slider, from_=0, to=100, orient="horizontal",
                                 variable=self.vol_var, command=self.on_volume_change)
        self.scl_vol.pack(side="left", fill="x", expand=True)
        self.lbl_vol = ttk.Label(frm_slider, text="80%", width=6)
        self.lbl_vol.pack(side="left", padx=4)

        # 朗读文本显示
        frm_text = ttk.LabelFrame(self.root, text=" 正在朗读 ")
        frm_text.pack(fill="both", expand=True, **pad)
        self.txt_show = tk.Text(frm_text, height=10, wrap="word",
                                font=("Microsoft YaHei UI", 13), relief="flat")
        self.txt_show.pack(fill="both", expand=True, padx=6, pady=6)
        self.txt_show.tag_configure("mark", foreground="#2f6fbf")

        # 进度
        frm_prog = ttk.Frame(self.root)
        frm_prog.pack(fill="x", **pad)
        self.progress = ttk.Progressbar(frm_prog, mode="determinate")
        self.progress.pack(side="left", fill="x", expand=True, padx=6)
        self.lbl_prog = ttk.Label(frm_prog, text="0/0")
        self.lbl_prog.pack(side="left", padx=6)

        # 控制按钮
        frm_btn = ttk.Frame(self.root)
        frm_btn.pack(fill="x", **pad)
        self.btn_play = ttk.Button(frm_btn, text="▶ 开始朗读", command=self.start_reading, width=12)
        self.btn_play.pack(side="left", padx=6)
        self.btn_pause = ttk.Button(frm_btn, text="⏸ 暂停", command=self.toggle_pause, width=12)
        self.btn_pause.pack(side="left", padx=6)
        ttk.Button(frm_btn, text="⏹ 停止", command=self.stop_reading, width=12).pack(side="left", padx=6)
        ttk.Button(frm_btn, text="导出整本MP3…", command=self.export_mp3, width=14).pack(side="right", padx=6)

        # 状态栏
        self.var_status = tk.StringVar(value="就绪")
        ttk.Label(self.root, textvariable=self.var_status,
                  anchor="w", relief="sunken").pack(fill="x", side="bottom")

    # ================== 配置存取 ==================
    def _load_config(self):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"progress": {}}

    def _save_config(self):
        try:
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump(self.config, f, ensure_ascii=False, indent=1)
        except Exception:
            pass

    def _save_progress(self):
        if not self.file_path:
            return
        offset = sum(len(c) for c in self.chunks[:self.index])
        prog = self.config.setdefault("progress", {})
        prog[os.path.abspath(self.file_path)] = {
            "offset": offset,
            "mtime": os.path.getmtime(self.file_path) if os.path.exists(self.file_path) else 0,
        }
        self.config["voice"] = self.var_voice.get() and self._voice_id()
        self.config["rate"] = int(self.rate_var.get())
        self.config["volume"] = round(self.vol_var.get() / 100, 2)
        self._save_config()

    def _voice_id(self):
        name = self.var_voice.get()
        return VOICE_LOOKUP.get(name, self.voice)

    # ================== 动作 ==================
    def open_file(self):
        if self.reading:
            self.stop_reading()
        path = filedialog.askopenfilename(
            title="选择小说文件",
            filetypes=[("文本文件", "*.txt *.md"), ("所有文件", "*.*")],
        )
        if not path:
            return
        try:
            raw = open(path, "rb").read()
            enc = chardet.detect(raw)["encoding"] or "utf-8"
            try:
                text = raw.decode(enc)
            except Exception:
                text = raw.decode("utf-8", errors="replace")
            if not text.strip():
                messagebox.showwarning("提示", "文件内容为空。")
                return
            self.chunks = split_into_chunks(text)
            self.file_path = path
            self.index = 0
            self.var_file.set(path)
            self.var_status.set(f"已载入 {len(self.chunks)} 段 · {len(text)} 字")

            # 尝试续读
            saved = self.config.get("progress", {}).get(os.path.abspath(path))
            if saved and saved.get("offset"):
                self.index = self._offset_to_index(saved["offset"])
                self.var_status.set(
                    f"已载入 {len(self.chunks)} 段，已定位到上次进度 (第 {self.index} 段)")
            self._update_progress_bar()
        except Exception as e:
            messagebox.showerror("打开失败", str(e))

    @staticmethod
    def _offset_to_index(chunks, offset):
        total = 0
        for i, c in enumerate(chunks):
            if total >= offset:
                return i
            total += len(c)
        return len(chunks)

    def restart(self):
        if self.reading:
            self.stop_reading()
        self.index = 0
        self._update_progress_bar()
        self.var_status.set("已重置到开头")
        self.start_reading()

    def _current_chunk(self):
        return self.chunks[self.index] if 0 <= self.index < len(self.chunks) else ""

    def start_reading(self):
        if self.reading:
            return
        if not self.chunks:
            messagebox.showwarning("提示", "请先打开一本小说。")
            return
        if self.index >= len(self.chunks):
            self.index = 0
        self.stop_flag.clear()
        self.pause_flag.clear()
        self.reading = True
        self.requested = set()
        # 预取设置，避免后台线程访问 tkinter 变量
        self._voice = self._voice_id()
        self._rate_str = f"{int(self.rate_var.get()):+d}%"
        self.worker = SynthWorker(self.tmpdir)
        self.worker.start()
        threading.Thread(target=self._reader_loop, daemon=True).start()
        self.btn_play.config(state="disabled")
        self.var_status.set("正在朗读…")

    def stop_reading(self):
        self.stop_flag.set()
        self.pause_flag.clear()
        pygame.mixer.music.stop()
        if self.worker:
            self.worker.stop()
            self.worker = None
        self.reading = False
        self.btn_play.config(state="normal")
        self.var_status.set("已停止")
        self._save_progress()

    def toggle_pause(self):
        if not self.reading:
            return
        if self.pause_flag.is_set():
            self.pause_flag.clear()
            self.btn_pause.config(text="⏸ 暂停")
            self.var_status.set("继续朗读…")
        else:
            self.pause_flag.set()
            self.btn_pause.config(text="▶ 继续")
            self.var_status.set("已暂停")

    def on_rate_change(self, _=None):
        v = int(self.rate_var.get())
        self.lbl_rate.config(text=f"{v:+d}%")

    def on_volume_change(self, _=None):
        v = int(self.vol_var.get())
        self.lbl_vol.config(text=f"{v}%")
        if pygame.mixer.get_init():
            pygame.mixer.music.set_volume(v / 100)

    def preview_voice(self):
        if self.reading:
            messagebox.showinfo("提示", "朗读中暂不能试听，请先停止。")
            return
        voice = self._voice_id()
        self.var_status.set("试听中…")
        threading.Thread(target=self._preview_thread, args=(voice,), daemon=True).start()

    def _preview_thread(self, voice):
        try:
            path = SynthWorker._synth_one("你好，我是" + self._voice_name(voice) + "，欢迎使用小说朗读器。", voice, f"{int(self.rate_var.get()):+d}%")
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(self.vol_var.get() / 100)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            try:
                os.remove(path)
            except OSError:
                pass
            self.ui_queue.put(lambda: self.var_status.set("就绪"))
        except Exception as e:
            self.ui_queue.put(lambda: messagebox.showerror("试听失败", f"请检查网络：\n{e}"))

    def _voice_name(self, vid):
        for i, n in STATIC_VOICES:
            if i == vid:
                return n.split(" · ")[0]
        return vid

    def export_mp3(self):
        if not self.chunks:
            messagebox.showwarning("提示", "请先打开一本小说。")
            return
        if self.reading:
            messagebox.showinfo("提示", "请先停止朗读。")
            return
        outdir = filedialog.askdirectory(title="选择导出文件夹")
        if not outdir:
            return
        voice = self._voice_id()
        rate = f"{int(self.rate_var.get()):+d}%"
        threading.Thread(target=self._export_thread, args=(outdir, voice, rate), daemon=True).start()

    def _export_thread(self, outdir, voice, rate):
        self.ui_queue.put(lambda: self.var_status.set("导出中…请稍候"))
        total = len(self.chunks)
        ok = 0
        for i, chunk in enumerate(self.chunks):
            try:
                path = SynthWorker._synth_one(chunk, voice, rate)
                dst = os.path.join(outdir, f"part{i+1:04d}.mp3")
                os.replace(path, dst)
                ok += 1
            except Exception:
                continue
            self.ui_queue.put(lambda n=i, t=total: self.var_status.set(f"导出中 {n+1}/{t}"))
        self.ui_queue.put(lambda: (messagebox.showinfo("完成", f"已导出 {ok}/{total} 段到：\n{outdir}"),
                                   self.var_status.set("就绪")))

    # ================== 朗读主循环 ==================
    def _reader_loop(self):
        try:
            while not self.stop_flag.is_set():
                if self.pause_flag.is_set():
                    time.sleep(0.05)
                    continue
                if self.index >= len(self.chunks):
                    self.ui_queue.put(self._on_finished)
                    return
                # 确保当前段已提交合成
                if self.index not in self.requested:
                    self.requested.add(self.index)
                    self.worker.request(self.index, self.chunks[self.index], self._voice, self._rate_str)
                # 取当前段音频
                path = self.worker.get(self.index, timeout=60)
                if path is None:
                    self.ui_queue.put(self._on_synth_error)
                    return
                # 后台预生成下一段（双缓冲，无缝衔接）
                nxt = self.index + 1
                if nxt < len(self.chunks) and nxt not in self.requested:
                    self.requested.add(nxt)
                    self.worker.request(nxt, self.chunks[nxt], self._voice, self._rate_str)
                # 更新界面显示当前段落
                self.ui_queue.put(lambda i=self.index: self._show_chunk(i))

                pygame.mixer.music.load(path)
                pygame.mixer.music.set_volume(self.vol_var.get() / 100)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() and not self.stop_flag.is_set():
                    if self.pause_flag.is_set():
                        pygame.mixer.music.pause()
                        while self.pause_flag.is_set() and not self.stop_flag.is_set():
                            time.sleep(0.05)
                        pygame.mixer.music.unpause()
                    time.sleep(0.05)
                self.index += 1
                if self.index % 10 == 0 or self.index >= len(self.chunks):
                    self._save_progress()
                self.ui_queue.put(lambda: self._update_progress_bar())
                try:
                    os.remove(path)
                except OSError:
                    pass
            # 停止
            self.reading = False
            self.ui_queue.put(self._set_idle)
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.reading = False
            self.ui_queue.put(lambda: self.var_status.set(f"播放出错：{e}"))

    def _on_finished(self):
        self.reading = False
        self.btn_play.config(state="normal")
        self.btn_pause.config(text="⏸ 暂停")
        self.var_status.set("全书朗读完毕 🎉")
        self._save_progress()
        messagebox.showinfo("完成", "全书朗读完毕！")

    def _on_synth_error(self):
        self.reading = False
        self.btn_play.config(state="normal")
        self.var_status.set("语音合成失败（请检查网络）")
        messagebox.showerror("错误", "语音合成失败，请检查网络连接后重试。")
        self._save_progress()

    def _set_idle(self):
        self.reading = False
        self.btn_play.config(state="normal")
        self.btn_pause.config(text="⏸ 暂停")

    # ================== 界面更新 ==================
    def _show_chunk(self, i):
        self.txt_show.delete("1.0", "end")
        self.txt_show.insert("1.0", self.chunks[i] if i < len(self.chunks) else "")
        self.txt_show.tag_add("mark", "1.0", "end")
        self._update_progress_bar()

    def _update_progress_bar(self):
        total = len(self.chunks)
        self.progress.config(maximum=max(total, 1), value=min(self.index, total))
        self.lbl_prog.config(text=f"{min(self.index, total)}/{total} 段")

    def _poll_ui_queue(self):
        try:
            while True:
                fn = self.ui_queue.get_nowait()
                try:
                    fn()
                except Exception:
                    pass
        except queue.Empty:
            pass
        self.root.after(100, self._poll_ui_queue)

    def _apply_settings(self):
        self.lbl_rate.config(text=f"{int(self.rate_var.get()):+d}%")
        self.lbl_vol.config(text=f"{int(self.vol_var.get())}%")

    def _refresh_voices(self):
        """联网获取完整音色列表并合并到下拉框（后台，失败则忽略）。"""
        try:
            loop = asyncio.new_event_loop()
            try:
                voices = loop.run_until_complete(edge_tts.list_voices())
            finally:
                loop.close()
            fresh = [v for v in voices if v["Locale"].startswith("zh-")]
            names = {}
            for v in fresh:
                nm = f"{v['ShortName']} · {v['Gender']} · {v['Locale']}"
                names[nm] = v["ShortName"]
            if names:
                self.ui_queue.put(lambda: self._merge_voices(names))
        except Exception:
            pass

    def _merge_voices(self, names):
        existing = list(self.cmb_voice["values"])
        merged = existing[:]
        for name in names:
            if name not in merged:
                merged.append(name)
        self.cmb_voice["values"] = merged
        VOICE_LOOKUP.update(names)
        self.var_status.set("已刷新完整音色列表")

    def refresh_voices_manual(self):
        self.var_status.set("刷新音色列表…")
        threading.Thread(target=self._refresh_voices, daemon=True).start()

    def on_close(self):
        self.stop_reading()
        try:
            pygame.mixer.quit()
        except Exception:
            pass
        try:
            import shutil
            shutil.rmtree(self.tmpdir, ignore_errors=True)
        except Exception:
            pass
        self.root.destroy()


def main():
    root = tk.Tk()
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass
    NovelReaderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
