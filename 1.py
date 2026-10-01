import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# ===================== 1. 改为你图片中的DH变换矩阵形式 =====================
# 对应公式: _{i}^{i-1}T = Rot(x,α_{i-1})·Trans(x,a_{i-1})·Rot(z,θ_i)·Trans(z,d_i)
def dh_matrix(a_prev, alpha_prev, d_i, theta_i):
    cθ = np.cos(theta_i)
    sθ = np.sin(theta_i)
    cα = np.cos(alpha_prev)
    sα = np.sin(alpha_prev)
    return np.array([
        [cθ,              -sθ,               0,            a_prev        ],
        [sθ*cα,           cθ*cα,            -sα,          -d_i*sα       ],
        [sθ*sα,           cθ*sα,             cα,           d_i*cα        ],
        [0,                0,                0,            1             ]
    ])

# ===================== 2. 固定机械臂DH参数（严格对应你的表格） =====================
# 结构尺寸（可自行修改）
b, h, a, L1, L2 = 1.0, 1.0, 1.0, 1.0, 1.0
# 坐标系标签
labels = ['基系i0', 'i1(le)', 'i2(f2)', 'i3', 'i4', 'i5(跳跃)', '末端Lx']
# 坐标轴颜色 X-红 Y-绿 Z-蓝
colors = ['r', 'g', 'b']
axis_len = 0.4  # 坐标系轴长度

# ===================== 3. 初始化画布 =====================
fig = plt.figure(figsize=(12, 10))
# 主3D绘图区域
ax_3d = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)  # 底部留出空间放滑块

# 滑块位置（底部横向排列）
ax_theta1 = plt.axes([0.18, 0.15, 0.65, 0.03])
ax_theta2 = plt.axes([0.18, 0.10, 0.65, 0.03])
ax_theta3 = plt.axes([0.18, 0.05, 0.65, 0.03])

# 初始化滑块（角度范围 -π ~ π）
theta1_slider = Slider(ax_theta1, 'θ₁ (le)', -np.pi, np.pi, valinit=0.0)
theta2_slider = Slider(ax_theta2, 'θ₂ (f2)', -np.pi, np.pi, valinit=0.0)
theta3_slider = Slider(ax_theta3, 'θ₃ (跳跃)', -np.pi, np.pi, valinit=0.0)

# ===================== 4. 核心：更新绘图函数（滑块拖动时自动调用） =====================
def update(val):
    # 获取当前滑块角度
    θ1 = theta1_slider.val
    θ2 = theta2_slider.val
    θ3 = theta3_slider.val
    
    # 你的DH参数表（参数顺序: [a_{i-1}, α_{i-1}, d_i, θ_i]）
    dh_params = [
        [b,    0,      -h,    np.pi/2],   # i0
        [a,    np.pi/2, 0,    θ1 ],      # i1
        [0,   -np.pi/2, 0,    0],      # i2
        [0,    np.pi/2, 0,     0],       # i3
        [0,    0 +θ2,      0,    -np.pi/2],  # i4
        [L1,   0,      0,     θ3],       # i5
        [L2,   0,      0,     0]         # 末端
    ]
    
    # 计算累积变换矩阵 + 各坐标系原点
    T_total = np.eye(4)
    transforms = [T_total]
    for param in dh_params:
        T_dh = dh_matrix(*param)
        T_total = T_total @ T_dh
        transforms.append(T_total)
    
    # 获取所有坐标系原点（包含基系 + 所有关节 + L2末端）
    origins = [T[:3, 3] for T in transforms]
    
    # 清空3D画布重绘
    ax_3d.cla()
    
    # 绘制所有坐标系
    for i, T in enumerate(transforms[:-1]):  # 坐标系只画到标签数量
        orig = origins[i]
        x_axis = T[:3, 0]
        y_axis = T[:3, 1]
        z_axis = T[:3, 2]
        
        ax_3d.quiver(*orig, *x_axis, length=axis_len, color=colors[0], linewidth=2)
        ax_3d.quiver(*orig, *y_axis, length=axis_len, color=colors[1], linewidth=2)
        ax_3d.quiver(*orig, *z_axis, length=axis_len, color=colors[2], linewidth=2)
        ax_3d.text(*orig, labels[i], fontsize=9)
    
    # 绘制完整连杆（包含最后一段L2的边）
    origins_np = np.array(origins)
    ax_3d.plot(origins_np[:, 0], origins_np[:, 1], origins_np[:, 2],
              'o-', color='gray', linewidth=3, markersize=5)
    
    # 3D图设置
    ax_3d.set_xlabel('X')
    ax_3d.set_ylabel('Y')
    ax_3d.set_zlabel('Z')
    ax_3d.set_xlim(-2, 4)
    ax_3d.set_ylim(-2, 4)
    ax_3d.set_zlim(-2, 4)
    ax_3d.set_title('DH坐标系实时可视化（已使用你提供的变换矩阵形式）', fontsize=12)

# 绑定滑块与更新函数
theta1_slider.on_changed(update)
theta2_slider.on_changed(update)
theta3_slider.on_changed(update)

# 初始化绘图
update(0)
plt.show()