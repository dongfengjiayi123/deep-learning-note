"""
Q-Table 强化学习算法（Q-Learning）
适配最新 Gymnasium API
环境：FrozenLake-v1（冰湖行走，4x4网格）
"""
import time
import gymnasium as gym  # 替换旧版gym，解决警告
import numpy as np

# 1. 创建冰湖环境
env = gym.make('FrozenLake-v1')

# 2. 全局配置
render = False
num_episodes = 10000
rList = []
running_reward = None

# 3. Q表初始化
Q = np.zeros([env.observation_space.n, env.action_space.n])

# 4. 超参数
lr = 0.85
gamma = 0.99
max_steps_per_episode = 99

# ===================== 开始训练 =====================
print("开始Q-Table训练...")
for episode in range(num_episodes):
    start_time = time.time()
    # 修复点1：新版reset返回 (state, info)
    state, _ = env.reset()
    total_reward = 0
    done = False

    for step in range(max_steps_per_episode):
        # 带噪声贪心策略
        noise = np.random.randn(1, env.action_space.n) * (1.0 / (episode + 1))
        action = np.argmax(Q[state, :] + noise)

        # 修复点2：新版step返回 5个参数
        next_state, reward, terminated, truncated, _ = env.step(action)
        # 合并结束条件
        done = terminated or truncated

        # Q-Learning核心更新
        Q[state, action] = Q[state, action] + lr * (
            reward + gamma * np.max(Q[next_state, :]) - Q[state, action]
        )

        total_reward += reward
        state = next_state

        if done:
            break

    # 记录奖励
    rList.append(total_reward)
    if running_reward is None:
        running_reward = total_reward
    else:
        running_reward = running_reward * 0.99 + total_reward * 0.01

    # 打印日志
    if episode % 100 == 0:
        print(f"轮次 [{episode}/{num_episodes}] | 总奖励: {total_reward:.2f} | 滑动平均奖励: {running_reward:.4f} | 耗时: {time.time()-start_time:.4f}s")

# ===================== 训练结束 =====================
print("\n训练完成！")
print(f"最终平均奖励: {sum(rList)/num_episodes:.4f}")
print("\n最终Q表值 (行=状态，列=动作[上/右/下/左]):")
print(np.round(Q, 4))

env.close()