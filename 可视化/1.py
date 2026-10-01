import matplotlib.pyplot as plt
import numpy as np

# 1. 加载数据
res = np.load("可视化\国民经济核算季度数据.npz", allow_pickle=True)
columns = res["columns"]
values = res["values"]

# 2. 全局配置：解决中文显示问题
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 3. 创建画布（设置尺寸：宽12，高6）
plt.figure(figsize=(12, 6))

# 4. 准备坐标轴数据
x = np.arange(1, values.shape[0] + 1)  # 季度序号
y = values[:, 3:6]                     # 三大产业产值
# 绘制饼图
plt.figure(figsize=(6, 6))
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False

labels = ['第一产业', '第二产业', '第三产业']

plt.pie(values[-1, 3:6], explode=[0.01, 0.01, 0.01], labels=labels, autopct='%1.1f%%')
plt.title('2017年第一季度各产业生产总值饼图')
plt.show()
# 5. 绘制折线图（自定义颜色，更美观）
plt.plot(x, y[:, 0], color="red", label="第一产业")
plt.plot(x, y[:, 1], color="blue", label="第二产业")
plt.plot(x, y[:, 2], color="green", label="第三产业")

# 6. 图表装饰
plt.title("2000-2017年各产业季度生产总值走势图", fontsize=14)
plt.xlabel("季度", fontsize=12)
plt.ylabel("生产总值（亿元）", fontsize=12)
plt.legend(loc="upper left")  # 图例：左上角

# 7. 优化x轴刻度（每年显示一次）
xticks_time = values[:, 1]
plt.xticks(x[::4], xticks_time[::4], rotation=45, ha="center")

# 8. 先保存图片，再展示（核心修复！）
plt.tight_layout()  # 自动调整布局，防止文字被截断
plt.savefig("./2000-2017年各产业季度生产总值走势图.png", dpi=300)
plt.show()




import numpy as np
import matplotlib.pyplot as plt
import os


# 绘图配置
plt.figure(figsize=(10, 6))
plt.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制散点图（增加颜色区分）
plt.scatter(values[:, 1], values[:, 3], marker='o', color='#1f77b4', label='第一产业生产总值')
plt.scatter(values[:, 1], values[:, 4], marker='*', color='#ff7f0e', label='第二产业生产总值')
plt.scatter(values[:, 1], values[:, 5], marker='D', color='#2ca02c', label='第三产业生产总值')

# 动态设置x轴刻度
data_len = len(values)
plt.xticks(range(0, data_len, 1), values[range(0, data_len, 1), 1], rotation=45, fontsize=8)

# 图表美化
plt.legend()
plt.title('2000-2017年各产业生产总值散点图', fontsize=14)
plt.ylabel('生产总值（亿元）', fontsize=12)
plt.grid(alpha=0.3, linestyle='--')
plt.tight_layout()  # 自动调整布局，避免标签被截断

# 保存并显示

plt.show()
# 绘制折线图
plt.figure(figsize=(8, 6))  # 创建画布，设置尺寸
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示（解决中文乱码）
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示异常

# 绘制三条折线，分别对应三大产业
plt.plot(values[:, 1], values[:, 3], linestyle='solid')  # 第一产业
plt.plot(values[:, 1], values[:, 4], marker='*')         # 第二产业
plt.plot(values[:, 1], values[:, 5], marker='D')         # 第三产业

# 设置x轴刻度：每4个季度（1年）显示一个时间标签，旋转45度防重叠
plt.xticks(range(0, 70, 4), values[range(0, 70, 4), 1], rotation=45)
plt.legend(['第一产业生产总值', '第二产业生产总值', '第三产业生产总值'])  # 添加图例
plt.title('2000-2017年各产业生产总值散点图')  # ❌ 标题错误，应该是折线图
plt.ylabel('生产总值（亿元）')  # 设置y轴标签

plt.show()  # 显示图表
