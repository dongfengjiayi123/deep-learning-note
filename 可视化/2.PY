# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# ===================== 全局设置：解决中文 =====================
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文
plt.rcParams['axes.unicode_minus'] = False    # 负号

# ===================== 1. 加载数据 =====================
res = np.load("可视化/国民经济核算季度数据.npz", allow_pickle=True)
columns = res["columns"]
values = res["values"]

# ===================== 图表1：三大产业季度走势折线图 =====================
plt.figure(figsize=(12, 6))
x = np.arange(1, values.shape[0] + 1)
y = values[:, 3:6]

plt.plot(x, y[:, 0], color="red", label="第一产业")
plt.plot(x, y[:, 1], color="blue", label="第二产业")
plt.plot(x, y[:, 2], color="green", label="第三产业")

plt.title("2000-2017年各产业季度生产总值走势图", fontsize=14)
plt.xlabel("季度", fontsize=12)
plt.ylabel("生产总值（亿元）", fontsize=12)
plt.legend(loc="upper left")

# X轴刻度：每年显示一次
xticks_time = values[:, 1]
plt.xticks(x[::4], xticks_time[::4], rotation=45, ha="center")

plt.tight_layout()
plt.savefig("./2000-2017年各产业季度生产总值走势图.png", dpi=300)

# ===================== 图表2：2017年第一季度饼图 =====================
plt.figure(figsize=(6, 6))
labels = ['第一产业', '第二产业', '第三产业']
plt.pie(values[-1, 3:6], 
        explode=[0.01, 0.01, 0.01], 
        labels=labels, 
        autopct='%1.1f%%',
        colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('2017年第一季度各产业生产总值饼图')

# ===================== 图表3：文本 + 数学公式演示（修复版） =====================
fig = plt.figure(figsize=(8, 6))
fig.suptitle('国民经济核算文本演示', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)

ax.set_title('子图标题')
ax.set_xlabel('X轴标签')
ax.set_ylabel('Y轴标签')

# 带框斜体文本
ax.text(3, 8, 'boxed italics text in data coords', 
        style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

# LaTeX数学公式（修复版）
ax.text(2, 6, r'an equation: $W = a \times 10^{-7}V^2$', color='red', fontsize=12)

# 普通Unicode文本（Python3 直接写，不用unicode()）
ax.text(3, 2, 'unicode: Institut für Festkörperphysik', fontsize=12)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# ===================== 最后统一展示 =====================
plt.show()