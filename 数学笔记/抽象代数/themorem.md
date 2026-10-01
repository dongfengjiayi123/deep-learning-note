# Smith 标准形（存在性）

&gt; **目标**：证明任意矩阵 $A\in M_{m\times n}(D)$（$D$ 为 PID）可通过左右乘可逆矩阵变为对角形式  
&gt; $$U A V = \operatorname{diag}(d_1,d_2,\dots,d_r,0,\dots,0)$$  
&gt; 且满足 $d_1\mid d_2\mid\cdots\mid d_r$（称为 **Smith 对角元**或**不变量因子**）。

---

## 先决知识与记号

- **$D$**：主理想整域（Principal Ideal Domain, PID）。
- **理想包含与整除**：对 $a,b\in D$，$(a)\subseteq(b) \iff b\mid a$。
- **Unimodular 矩阵**：在 $D$ 上可逆的方阵（行列式为单位元 $\in D^\times$）。左右乘 unimodular 矩阵 $\iff$ 初等行列变换。
- **记号**：$\operatorname{ent}_{ij}(A)$ 或 $a_{ij}$ 表示矩阵 $A$ 的第 $(i,j)$ 元素。

---

## 定理（Smith 标准形存在性）

对任意 $A\in M_{m\times n}(D)$，存在可逆矩阵 $P\in GL_m(D)$、$Q\in GL_n(D)$，使得
$$
P A Q = \begin{pmatrix}
d_1 &        &        &   \\
    & d_2    &        &   \\
    &        & \ddots &   \\
    &        &        & d_r \\
    &        &        &   & 0
\end{pmatrix},
\quad d_1\mid d_2\mid\cdots\mid d_r.
$$

---

## 证明思路（算法化）

将证明视为**矩阵版的欧几里得算法 + 归纳**：

### Step 1: 定位"最小"非零元
在所有非零元素中选取 $a_{kl}$ 使得理想 $(a_{kl})$ 在包含序上**极小**（即不存在其他非零元 $a_{ij}$ 使 $(a_{kl})\subsetneq (a_{ij})$）。通过交换行列将其移至 $(1,1)$ 位置。

### Step 2: Bézout 构造降低理想
若 $a_{11}\nmid a_{1k}$（某列情形，行同理），设 $d=\gcd(a_{11},a_{1k})$。写
$$a_{11}=a'_{11}d,\quad a_{1k}=a'_{1k}d.$$
由 PID 的 Bézout 性质，存在 $u,v\in D$ 使
$$u a'_{11} + v a'_{1k} = 1 \implies u a_{11} + v a_{1k} = d.$$

**构造列变换矩阵 $Q$**：取单位矩阵 $I_n$，将第 $(1,k)$ 列对应的 $2\times 2$ 块替换为
$$
\begin{pmatrix} u & -a'_{1k} \\ v & a'_{11} \end{pmatrix},
$$
即
$$
Q = I_n + (u-1)E_{11} + (a'_{11}-1)E_{kk} + vE_{k1} - a'_{1k}E_{1k}.
$$

**验证**：
- 新 $(1,1)$ 元素：$u\cdot a_{11} + v\cdot a_{1k} = d$
- 新 $(1,k)$ 元素：$-a'_{1k}\cdot a_{11} + a'_{11}\cdot a_{1k} = -a'_{1k}a'_{11}d + a'_{11}a'_{1k}d = 0$
- $\det(Q)=ua'_{11}+va'_{1k}=1$，故 $Q\in GL_n(D)$。

### Step 3: 终止性（关键！）
每次执行 Step 2：
- 要么左上角理想严格减小：$(d)\subsetneq (a_{11})$
- 要么某位置被清零

PID 中**不存在无限严格下降的理想链**（Noetherian 性），故有限步后必达状态：$a_{11}\mid$ 第 1 行所有元素且 $a_{11}\mid$ 第 1 列所有元素。

### Step 4: 清零第一行/列
当 $a_{11}$ 整除同行同列所有元素时，用初等变换（减倍消去）可得
$$
\begin{pmatrix} a_{11} & 0 \\ 0 & B \end{pmatrix}.
$$

### Step 5: 归纳
对子矩阵 $B$ 重复上述过程。由归纳假设，$B$ 可化为 Smith 形 $\operatorname{diag}(d_2,\dots,d_r,0,\dots,0)$ 且 $d_2\mid\cdots\mid d_r$。

**整除性传递**：因 $a_{11}$ 整除 $B$ 中所有元素（Step 4 保证），故 $a_{11}\mid d_2$。令 $d_1=a_{11}$，即得 $d_1\mid d_2\mid\cdots\mid d_r$。

---

## 精炼版证明（考场/笔记用）

&gt; **定理**：PID 上任意矩阵可通过初等变换化为 Smith 标准形。

**证**：对 $A\in M_{m\times n}(D)$ 的 $\min(m,n)$ 归纳。

1. **基例**：零矩阵已是 Smith 形。

2. **归纳步**：
   - 若非零，取非零元中生成理想极小者，换至 $(1,1)$，记为 $a$。
   - 若 $a$ 不整除某同行/列元素 $b$，设 $d=\gcd(a,b)=(ua+vb)$。构造 $2\times 2$ unimodular 块变换，将 $(1,1)$ 变为 $d$（理想严格减小），$(1,k)$ 或 $(k,1)$ 变为 0。
   - 由 PID 的 ACC（升链条件），有限步后 $a\mid$ 同行同列所有元。
   - 消去第 1 行第 1 列其余元，得块对角 $\begin{pmatrix} a & 0 \\ 0 & B \end{pmatrix}$。
   - 对 $B$ 用归纳假设得 Smith 形，且 $a\mid$ 所有不变量因子，故整除性保持。

3. **结论**：存在 $P,Q$ 可逆，使 $PAQ=\operatorname{diag}(d_1,\dots,d_r,0,\dots,0)$ 且 $d_1\mid\cdots\mid d_r$。 $\square$

---

## 补充说明

| 概念 | 说明 |
|------|------|
| **不变量因子** (Invariant Factors) | Smith 对角元 $d_1,\dots,d_r$ 本身 |
| **初等因子** (Elementary Divisors) | 将各 $d_i$ 分解为素元幂次的乘积 $d_i = \prod p_j^{e_{ij}}$，每个 $p_j^{e_{ij}}$ 称为初等因子 |
| **唯一性** | Smith 形在不计单位因子（associate）意义下唯一，可由行列式因子 $\Delta_k = \gcd(\text{所有 } k\times k \text{ 子式})$ 确定：$d_1=\Delta_1, d_1d_2=\Delta_2, \dots$ |

---

## 示例提示（手算练习）

对整数矩阵 $A=\begin{pmatrix} 12 & 8 \\ 6 & 10 \end{pmatrix}$：
1. $(12,6,8,10)$ 中理想极小元为 $6$（或 $8$？比较 $(6)=(6)$ 与 $(8)=(8)$，选 $6$ 换至 $(1,1)$）
2. $6\nmid 12$？实际 $6\mid 12$，但 $6\nmid 8$。$\gcd(6,8)=2$，构造变换降理想...
3. 最终可得 Smith 形 $\operatorname{diag}(2, 24)$（验证：$\det A=120-48=72=2\times 24$）

---

*生成时间：2026-02-26*