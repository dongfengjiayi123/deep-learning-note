---
title: 自信息、熵、联合熵与条件熵
aliases:
  - Self-information, Entropy, Joint Entropy and Conditional Entropy
  - 信息量与熵
  - 熵、联合熵与条件熵
created: 2026-07-27
updated: 2026-07-27
tags:
  - 信息论
  - 自信息
  - 熵
  - 联合熵
  - 条件熵
  - 概率论
status: 整理完成
chapter: 2.1
source_numbering: 原教材编号

---


# 2.1 自信息、熵、联合熵与条件熵

> [!abstract] 本节主线 从事件的**自信息**出发，说明信息量为何具有对数形式；随后定义离散随机变量的**熵**，并研究熵的非负性、最大值、联合熵、条件熵、链式法则、条件化不增熵以及独立随机变量熵的可加性。

---

## 索引导航

### 按教材编号索引

- [[#^thm-2-1|Theorem 2.1：自信息函数的唯一形式]]
    
- [[#^def-2-2|Definition 2.2：熵]]
    
- [[#^ex-2-3|Example 2.3：二元熵函数]]
    
- [[#^lem-2-4|Lemma 2.4：对数基本不等式]]
    
- [[#^lem-2-5|Lemma 2.5：熵的非负性]]
    
- [[#^lem-2-6|Lemma 2.6：熵的上界]]
    
- [[#^lem-2-7|Lemma 2.7：Log-sum 不等式]]
    
- [[#^def-2-8|Definition 2.8：联合熵]]
    
- [[#^def-2-9|Definition 2.9：条件熵]]
    
- [[#^thm-2-10|Theorem 2.10：熵的链式法则]]
    
- [[#^cor-2-11|Corollary 2.11：条件熵的链式法则]]
    
- [[#^lem-2-12|Lemma 2.12：条件化不增加熵]]
    
- [[#^lem-2-13|Lemma 2.13：独立随机变量的熵可加]]
    
- [[#^lem-2-14|Lemma 2.14：条件熵的次可加性]]
    

### 按知识主题索引

- [[#2.1.1 自信息（Self-information）|自信息]]
    
- [[#2.1.2 熵（Entropy）|熵]]
    
- [[#2.1.3 熵的基本性质|熵的基本性质]]
    
- [[#2.1.4 联合熵与条件熵|联合熵与条件熵]]
    
- [[#2.1.5 联合熵与条件熵的性质|联合熵与条件熵的性质]]
    
- [[#核心公式总表|核心公式总表]]
    
- [[#易错点总结|易错点总结]]
    

[!tip] 后续笔记中的引用方式 在其他笔记中可以直接写：

[[信息论_自信息与熵_Obsidian笔记#^thm-2-10|熵的链式法则]]  
[[信息论_自信息与熵_Obsidian笔记#^lem-2-12|条件化不增熵]]  
[[信息论_自信息与熵_Obsidian笔记#^eq-2-1-8|联合熵次可加公式]]

---

## 2.1.1 自信息（Self-information）

设 $E$ 是某一概率空间中的事件，其概率为

$$  
p_E:=\Pr(E),\qquad 0\le p_E\le 1.  
$$

  

事件 $E$ 的**自信息**记为 $I(E)$，表示：

1. 得知事件 $E$ 已发生时所获得的信息量；
    
2. 等价地，在得知 $E$ 发生之前，对其是否发生所具有的不确定程度。
    

直观上：

- 事件越常见，发生时带来的信息越少；
    
- 事件越罕见，发生时带来的信息越多；
    
- 必然事件不应提供新信息；
    
- 两个独立事件同时发生时，总信息量应等于二者信息量之和。
    

### 自信息应满足的公理

把信息量看成概率 $p$ 的函数 $I(p)$，通常要求：

1. **单调性**：$I(p)$ 关于 $p$ 单调递减；
    
2. **连续性**：$I(p)$ 关于 $p$ 连续；
    
3. **独立事件可加性**：若 $E_1,E_2$ 独立，则
    

$$  
I(E_1\cap E_2)=I(E_1)+I(E_2).  
$$

  

由于独立性意味着

$$  
\Pr(E_1\cap E_2)=\Pr(E_1)\Pr(E_2),  
$$

  

所以第三条也可以写成

$$  
I(p_1p_2)=I(p_1)+I(p_2).  
$$

  

### Theorem 2.1：自信息函数的唯一形式

> [!theorem] Theorem 2.1 对 $p\in(0,1]$，若函数 $I(p)$ 满足：
> 
> 1. $I(p)$ 关于 $p$ 单调递减；
>     
> 2. $I(p)$ 关于 $p$ 连续；
>     
> 3. $I(p_1p_2)=I(p_1)+I(p_2)$；
>     
> 
> 则存在常数 $c>0$，并可任取对数底数 $b>1$，使得
> 
> $$  
> I(p)=-c\log_b p.  
> $$
> 
>   

^thm-2-1

[!warning] 定义域中 $p=0$ 的问题 原文将定义域写成 $[0,1]$，但严格来说，实值函数 $I(p)$ 不可能在 $p=0$ 处连续，因为

$$  
\lim_{p\to0^+}-\log p=+\infty.  
$$

  

因此更严谨的写法是：

- 实值定义域取 $(0,1]$；
    
- 在扩展实数意义下约定 $I(0)=+\infty$。
    

#### Proof

令

$$  
f(t):=I(e^{-t}),\qquad t\ge 0.  
$$

  

由于

$$  
e^{-(s+t)}=e^{-s}e^{-t},  
$$

  

由可加性可得

$$  
\begin{aligned} f(s+t) &=I(e^{-(s+t)})\\ &=I(e^{-s}e^{-t})\\ &=I(e^{-s})+I(e^{-t})\\ &=f(s)+f(t). \end{aligned}  
$$

  

因此 $f$ 满足 Cauchy 加法方程。又因为 $I$ 连续，所以 $f$ 连续。连续的加法函数必为线性函数，故存在常数 $k$，使得

$$  
f(t)=kt.  
$$

  

令 $p=e^{-t}$，则 $t=-\ln p$，所以

$$  
I(p)=f(-\ln p)=-k\ln p.  
$$

  

由于 $I(p)$ 随 $p$ 增大而减小，因此 $k>0$。再利用换底公式

$$  
\log_b p=\frac{\ln p}{\ln b},  
$$

  

便可写成

$$  
I(p)=-c\log_b p,  
$$

  

其中 $c>0$。

#### 信息单位的选择

- 若取 $b=2,c=1$，则
    

$$  
I(p)=-\log_2p,  
$$

  

单位为 **bit**；

- 若取 $b=e,c=1$，则
    

$$  
I(p)=-\ln p,  
$$

  

单位为 **nat**。

> [!danger] 关于“$c$ 是 $\log_2$”的修正 “以 2 为底”并不意味着定理中的 $c=\log_2$。
> 
> - $c$ 是一个正的**数值常数**；
>     
> - $\log_2$ 是一个**函数**。
>     
> 
> 若使用 bit 作为单位，应取
> 
> $$  
> b=2,\qquad c=1.  
> $$
> 
>   
> 
> 若坚持使用自然对数表示 bit，则应写成
> 
> $$  
> I(p)=-\frac{1}{\ln 2}\ln p.  
> $$
> 
>   

由可加性还可得到

$$  
I(1)=I(1\cdot 1)=I(1)+I(1),  
$$

  

因此

$$  
I(1)=0.  
$$

  

也就是说，必然事件不携带新的信息。

---

## 2.1.2 熵（Entropy）

设离散随机变量 $X$ 取值于有限字母表 $\mathcal X$，其概率质量函数为

$$  
P_X(x):=\Pr(X=x),\qquad x\in\mathcal X.  
$$

  

### Definition 2.2：熵

> [!definition] Definition 2.2（Entropy） 随机变量 $X$ 的熵记为 $H(X)$ 或 $H(P_X)$，定义为
> 
> $$  
> H(X):=-\sum_{x\in\mathcal X}P_X(x)\log_2P_X(x).  
> $$
> 
>   
> 
> 当对数底数为 $2$ 时，熵的单位是 bit。

^def-2-2

对基本事件 ${X=x}$，其自信息为

$$  
I(x):=-\log_2P_X(x).  
$$

  

因此

$$  
H(X)=\mathbb E[-\log_2P_X(X)]=\mathbb E[I(X)].  
$$

  

^eq-entropy-expectation

所以，熵就是随机变量各个可能结果的自信息的概率加权平均，即：

> 熵表示在观察随机变量的一次实现后，平均能够获得多少信息。

### 零概率项的约定

计算熵时约定

$$  
0\log_2 0:=0.  
$$

  

这是因为

$$  
\lim_{x\to0^+}x\log_2x=0.  
$$

  

零概率事件不会实际发生，所以它对平均信息量的贡献为零。

### 熵只依赖于概率分布

$H(X)$ 只由 $X$ 的概率分布决定，与结果使用什么符号表示无关。

例如，公平硬币的两个结果可以记为 $0,1$，也可以记为 $2,100$。只要两个结果的概率仍为 $1/2$，熵始终为

$$  
H(X)=-2\cdot\frac12\log_2\frac12=1\text{ bit}.  
$$

  

### Example 2.3：二元熵函数

> [!example] Example 2.3 设二元随机变量 $X\in{0,1}$，且
> 
> $$  
> P_X(1)=p,\qquad P_X(0)=1-p,  
> $$
> 
>   
> 
> 其中 $0\le p\le1$。则
> 
> $$  
> H(X)=-p\log_2p-(1-p)\log_2(1-p).  
> $$
> 
>   
> 
> 该函数称为**二元熵函数**，记为
> 
> $$  
> h_b(p):=-p\log_2p-(1-p)\log_2(1-p).  
> $$
> 
>   

^ex-2-3

二元熵函数具有以下性质：

- $h_b(0)=h_b(1)=0$；
    
- $h_b(p)=h_b(1-p)$；
    
- 在 $p=1/2$ 处取得最大值；
    
- 最大值为
    

$$  
h_b\left(\frac12\right)=1\text{ bit}.  
$$

  

这说明：两个结果等概率时不确定性最大；某一结果必然发生时不确定性为零。

### bit 与 nat 的换算

若使用自然对数定义熵，则

$$  
H_e(X):=-\sum_xP_X(x)\ln P_X(x).  
$$

  

由于

$$  
\ln p=(\ln2)\log_2p,  
$$

  

所以

$$  
H_e(X)=(\ln2)H(X).  
$$

  

反过来，

$$  
H(X)=\frac{H_e(X)}{\ln2}=H_e(X)\log_2e.  
$$

  

因此

$$  
1\text{ bit}=\ln2\text{ nats},  
$$

  

$$  
1\text{ nat}=\log_2e\text{ bits}.  
$$

  

---

## 2.1.3 熵的基本性质

这一部分主要利用两个工具：

1. [[#^lem-2-4|对数基本不等式]]；
    
2. [[Jensen 不等式]]与函数 $f(t)=t\log t$ 的凸性。
    

### Lemma 2.4：对数基本不等式

> [!lemma] Lemma 2.4（Fundamental Inequality, FI） 对任意 $x>0$ 和 $D>1$，有
> 
> $$  
> \log_Dx\le \log_D(e)(x-1),  
> $$
> 
>   
> 
> 等号成立当且仅当 $x=1$。

^lem-2-4

#### Proof

由换底公式

$$  
\log_Dx=\frac{\ln x}{\ln D}=\log_D(e)\ln x,  
$$

  

所以只需证明

$$  
\ln x\le x-1.  
$$

  

令

$$  
g(x):=x-1-\ln x.  
$$

  

则

$$  
g'(x)=1-\frac1x=\frac{x-1}{x}.  
$$

  

因此 $g$ 在 $(0,1)$ 上递减，在 $(1,\infty)$ 上递增，并且

$$  
g(1)=0.  
$$

  

所以

$$  
g(x)\ge0,  
$$

  

即

$$  
\ln x\le x-1.  
$$

  

等号仅在 $x=1$ 时成立。

### Lemma 2.5：熵的非负性

> [!lemma] Lemma 2.5（Nonnegativity） 对任意离散随机变量 $X$，
> 
> $$  
> H(X)\ge0.  
> $$
> 
>   
> 
> 等号成立当且仅当 $X$ 是确定性随机变量。

^lem-2-5

#### Proof

因为

$$  
0\le P_X(x)\le1,  
$$

  

所以

$$  
\log_2P_X(x)\le0.  
$$

  

因此每一项均满足

$$  
-P_X(x)\log_2P_X(x)\ge0.  
$$

  

求和可得

$$  
H(X)\ge0.  
$$

  

若 $H(X)=0$，则所有正概率项都必须为零。对 $P_X(x)>0$，有

$$  
-P_X(x)\log_2P_X(x)=0,  
$$

  

这只能发生在 $P_X(x)=1$ 时。因此存在唯一一个结果以概率 $1$ 发生，即 $X$ 为确定性随机变量。

### Lemma 2.6：有限字母表上的熵上界

> [!lemma] Lemma 2.6（Upper Bound on Entropy） 若随机变量 $X$ 的取值集合为有限集 $\mathcal X$，则
> 
> $$  
> 0\le H(X)\le\log_2|\mathcal X|.  
> $$
> 
>   
> 
> 等号成立当且仅当 $X$ 在 $\mathcal X$ 上均匀分布。

^lem-2-6

#### Proof

令

$$  
m:=|\mathcal X|.  
$$

  

则

$$  
\begin{aligned} \log_2m-H(X) &=\sum_{x\in\mathcal X}P_X(x)\log_2m +\sum_{x\in\mathcal X}P_X(x)\log_2P_X(x)\\ &=\sum_{x\in\mathcal X}P_X(x)\log_2\bigl(mP_X(x)\bigr). \end{aligned}  
$$

  

在 Lemma 2.4 中令

$$  
z:=\frac{1}{mP_X(x)},  
$$

  

则

$$  
\log_2\frac{1}{mP_X(x)} \le \log_2(e)\left(\frac{1}{mP_X(x)}-1\right).  
$$

  

两边乘以 $-P_X(x)$，得到

$$  
P_X(x)\log_2\bigl(mP_X(x)\bigr) \ge \log_2(e)\left(P_X(x)-\frac1m\right).  
$$

  

对 $x$ 求和：

$$  
\begin{aligned} \log_2m-H(X) &\ge \log_2(e)\sum_x\left(P_X(x)-\frac1m\right)\\ &=\log_2(e)(1-1)\\ &=0. \end{aligned}  
$$

  

因此

$$  
H(X)\le\log_2m.  
$$

  

等号成立要求对所有 $P_X(x)>0$ 的 $x$，都有

$$  
\frac{1}{mP_X(x)}=1,  
$$

  

即

$$  
P_X(x)=\frac1m.  
$$

  

因此，等号成立当且仅当 $X$ 在 $\mathcal X$ 上均匀分布。

> [!intuition] 直观解释
> 
> - 确定性分布完全可以预测，因此熵为 $0$；
>     
> - 均匀分布中所有结果同样可能，最难预测，因此熵达到最大值 $\log_2m$。
> - 在本证明中可以参照凹函数的证明因为$\sum_{x}p(x)=1$那么根据凹函数的定义其小于组合的函数,其组合为
>     

### Lemma 2.7：Log-sum 不等式

> [!lemma] Lemma 2.7（Log-sum Inequality） 对非负数 $a_1,\dots,a_n$ 和 $b_1,\dots,b_n$，有
> 
> $$  
> \sum_{i=1}^na_i\log_D\frac{a_i}{b_i} \ge \left(\sum_{i=1}^na_i\right) \log_D \frac{\sum_{i=1}^na_i}{\sum_{i=1}^nb_i}.  
> $$
> 
>   
> 
> 在所有相关项为正时，等号成立当且仅当
> 
> $$  
> \frac{a_i}{b_i} = \frac{\sum_ja_j}{\sum_jb_j}  
> $$
> 
>   
> 
> 对所有 $i$ 都成立，即 $a_i/b_i$ 为常数。

^lem-2-7

采用以下约定：

$$  
0\log_D0=0,  
$$

  

$$  
0\log_D\frac00=0,  
$$

  

并且当 $a>0$ 时，

$$  
a\log_D\frac a0=+\infty.  
$$

  

#### Proof：利用 Jensen 不等式

先假设 $a_i>0,b_i>0$。令

$$  
A:=\sum_{j=1}^na_j, \qquad B:=\sum_{j=1}^nb_j,  
$$

  

并设置

$$  
\alpha_i:=\frac{b_i}{B}, \qquad t_i:=\frac{a_i}{b_i}, \qquad f(t):=t\log_Dt.  
$$

  

因为

$$  
f''(t)=\frac{1}{t\ln D}>0,  
$$

  

所以 $f$ 是严格凸函数。由 Jensen 不等式，

$$  
\sum_{i=1}^n\alpha_if(t_i) \ge f\left(\sum_{i=1}^n\alpha_it_i\right).  
$$

  

左边为

$$  
\frac1B\sum_{i=1}^na_i\log_D\frac{a_i}{b_i},  
$$

  

右边为

$$  
\frac AB\log_D\frac AB.  
$$

  

两边乘以 $B$，得到

$$  
\sum_{i=1}^na_i\log_D\frac{a_i}{b_i} \ge A\log_D\frac AB.  
$$

  

严格凸性说明等号成立当且仅当所有 $t_i$ 相同，即 $a_i/b_i$ 为常数。

> [!danger] 关于原笔记中证明思路的修正 Log-sum 不等式并不是由“均匀分布时熵最大”直接推出的。标准证明使用函数
> 
> $$  
> f(t)=t\log t  
> $$
> 
>   
> 
> 的凸性和 Jensen 不等式。

---

## 2.1.4 联合熵与条件熵

设随机变量 $(X,Y)$ 的联合概率质量函数为

$$  
P_{X,Y}(x,y),\qquad (x,y)\in\mathcal X\times\mathcal Y.  
$$

  

二维基本事件 ${X=x,Y=y}$ 的自信息定义为

$$  
I(x,y):=-\log_2P_{X,Y}(x,y).  
$$

  

### Definition 2.8：联合熵

> [!definition] Definition 2.8（Joint Entropy） 随机变量 $(X,Y)$ 的联合熵定义为
> 
> $$  
> H(X,Y) :=-\sum_{(x,y)\in\mathcal X\times\mathcal Y} P_{X,Y}(x,y)\log_2P_{X,Y}(x,y).  
> $$
> 
>   
> 
> 等价地，
> 
> $$  
> H(X,Y)=\mathbb E[-\log_2P_{X,Y}(X,Y)].  
> $$
> 
>   

^def-2-8

联合熵衡量同时描述 $X$ 和 $Y$ 所需的平均信息量。

### Definition 2.9：条件熵

> [!definition] Definition 2.9（Conditional Entropy） 已知 $X$ 后，$Y$ 的条件熵定义为
> 
> $$  
> H(Y\mid X) :=\sum_{x\in\mathcal X}P_X(x) \left[-\sum_{y\in\mathcal Y} P_{Y\mid X}(y\mid x)\log_2P_{Y\mid X}(y\mid x) \right].  
> $$
> 
>   

^def-2-9

条件熵还可以写成

$$  
H(Y\mid X) =-\sum_{x,y}P_{X,Y}(x,y) \log_2P_{Y\mid X}(y\mid x),  
$$

  

或

$$  
H(Y\mid X)=\mathbb E[-\log_2P_{Y\mid X}(Y\mid X)].  
$$

  

条件熵表示：观察到 $X$ 之后，关于 $Y$ 仍然剩余的平均不确定性。

### Theorem 2.10：熵的链式法则

> [!theorem] Theorem 2.10（Chain Rule for Entropy）
> 
> $$  
> H(X,Y)=H(X)+H(Y\mid X).  
> $$
> 
>   

^thm-2-10

#### Proof

由条件概率分解

$$  
P_{X,Y}(x,y)=P_X(x)P_{Y\mid X}(y\mid x),  
$$

  

有

$$  
\begin{aligned} H(X,Y) &=\mathbb E[-\log_2P_{X,Y}(X,Y)]\\ &=\mathbb E[-\log_2P_X(X)] +\mathbb E[-\log_2P_{Y\mid X}(Y\mid X)]\\ &=H(X)+H(Y\mid X). \end{aligned}  
$$

  

由于联合熵具有对称性，

$$  
H(X,Y)=H(Y,X),  
$$

  

所以

$$  
H(X)+H(Y\mid X)=H(Y)+H(X\mid Y).  
$$

  

因此

$$  
H(X)-H(X\mid Y)=H(Y)-H(Y\mid X).  
$$

  

这个共同的量将在后续定义为[[互信息]]：

$$  
I(X;Y):=H(X)-H(X\mid Y).  
$$

  

[!note] Equivocation 在通信系统中，$H(X\mid Y)$ 有时称为 **equivocation**，表示接收端观察 $Y$ 后，对信道输入 $X$ 仍然保留的不确定性。

### Corollary 2.11：条件熵的链式法则

> [!corollary] Corollary 2.11（Chain Rule for Conditional Entropy）
> 
> $$  
> H(X,Y\mid Z)=H(X\mid Z)+H(Y\mid X,Z).  
> $$
> 
>   

^cor-2-11

更一般地，

$$  
H(X_1,\dots,X_n) = \sum_{i=1}^nH(X_i\mid X_1,\dots,X_{i-1}).  
$$

  

---

## 2.1.5 联合熵与条件熵的性质

### Lemma 2.12：条件化不增加熵

> [!lemma] Lemma 2.12（Conditioning Never Increases Entropy）
> 
> $$  
> H(X\mid Y)\le H(X).  
> $$
> 
>   
> 
> 等号成立当且仅当 $X$ 与 $Y$ 独立。

^lem-2-12

这意味着：平均而言，获得额外信息 $Y$ 不会增加对 $X$ 的不确定性。

[!warning] 该结论不是逐点成立 条件化不增熵指的是

$$  
H(X\mid Y) =\sum_yP_Y(y)H(X\mid Y=y) \le H(X).  
$$

  

对某个特定的 $y$，完全可能出现

$$  
H(X\mid Y=y)>H(X).  
$$

  

#### Proof 1：利用熵的凹性

边缘分布可以写成条件分布的混合：

$$  
P_X(x)=\sum_yP_Y(y)P_{X\mid Y}(x\mid y).  
$$

  

即

$$  
P_X=\sum_yP_Y(y)P_{X\mid Y=y}.  
$$

  

熵关于概率分布是凹函数，因此

$$  
H\left(\sum_yP_Y(y)P_{X\mid Y=y}\right) \ge \sum_yP_Y(y)H(P_{X\mid Y=y}).  
$$

  

左边是 $H(X)$，右边是 $H(X\mid Y)$，所以

$$  
H(X)\ge H(X\mid Y).  
$$

  

若满足严格凹性的等号条件，则所有满足 $P_Y(y)>0$ 的条件分布都必须相同：

$$  
P_{X\mid Y}(x\mid y)=P_X(x).  
$$

  

这正是 $X$ 与 $Y$ 独立。

#### Proof 2：利用 Log-sum 不等式

先计算

$$  
\begin{aligned} H(X)-H(X\mid Y) &=\sum_{x,y}P_{X,Y}(x,y) \log_2\frac{P_{X\mid Y}(x\mid y)}{P_X(x)}\\ &=\sum_{x,y}P_{X,Y}(x,y) \log_2\frac{P_{X,Y}(x,y)}{P_X(x)P_Y(y)}. \end{aligned}  
$$

  

令

$$  
a_{x,y}:=P_{X,Y}(x,y), \qquad b_{x,y}:=P_X(x)P_Y(y).  
$$

  

由 Log-sum 不等式，

$$  
\begin{aligned} H(X)-H(X\mid Y) &\ge \left(\sum_{x,y}P_{X,Y}(x,y)\right) \log_2 \frac{\sum_{x,y}P_{X,Y}(x,y)} {\sum_{x,y}P_X(x)P_Y(y)}\\ &=1\cdot\log_2\frac11\\ &=0. \end{aligned}  
$$

  

所以

$$  
H(X\mid Y)\le H(X).  
$$

  

等号成立时，

$$  
\frac{P_{X,Y}(x,y)}{P_X(x)P_Y(y)}  
$$

  

在有效支撑集上必须为常数。因为分子和分母分别求和都等于 $1$，该常数只能为 $1$，于是

$$  
P_{X,Y}(x,y)=P_X(x)P_Y(y).  
$$

  

因此 $X$ 与 $Y$ 独立。

[!note] 与 KL 散度和互信息的联系 上述证明实际上给出

$$  
H(X)-H(X\mid Y) =D\bigl(P_{X,Y}\Vert P_XP_Y\bigr) =I(X;Y)\ge0.  
$$

  

参见：[[Kullback–Leibler 散度]]、[[互信息]]。

### Lemma 2.13：独立随机变量的熵可加

> [!lemma] Lemma 2.13 若 $X$ 与 $Y$ 独立，则
> 
> $$  
> H(X,Y)=H(X)+H(Y).  
> $$
> 
>   

^lem-2-13

#### Proof

独立性意味着

$$  
P_{Y\mid X}(y\mid x)=P_Y(y),  
$$

  

所以

$$  
H(Y\mid X)=H(Y).  
$$

  

结合链式法则，

$$  
H(X,Y)=H(X)+H(Y\mid X)=H(X)+H(Y).  
$$

  

更一般地，总有

$$  
H(X,Y) =H(X)+H(Y\mid X) \le H(X)+H(Y).  
$$

  

^eq-2-1-8

等号成立当且仅当 $X$ 与 $Y$ 独立。

### Lemma 2.14：条件熵的次可加性

> [!lemma] Lemma 2.14（Conditional Entropy Subadditivity）
> 
> $$  
> H(X_1,X_2\mid Y_1,Y_2) \le H(X_1\mid Y_1)+H(X_2\mid Y_2).  
> $$
> 
>   
> 
> 等号成立当且仅当
> 
> $$  
> P_{X_1,X_2\mid Y_1,Y_2}(x_1,x_2\mid y_1,y_2) = P_{X_1\mid Y_1}(x_1\mid y_1) P_{X_2\mid Y_2}(x_2\mid y_2)  
> $$
> 
>   
> 
> 对所有具有正条件概率的 $(y_1,y_2)$ 成立。

^lem-2-14

#### Proof

由条件熵的链式法则，

$$  
\begin{aligned} H(X_1,X_2\mid Y_1,Y_2) &=H(X_1\mid Y_1,Y_2) +H(X_2\mid X_1,Y_1,Y_2)\\ &\le H(X_1\mid Y_1,Y_2) +H(X_2\mid Y_1,Y_2). \end{aligned}  
$$

  

^eq-2-1-9

其中第一步不等式来自条件化不增加熵。再次应用条件化不增加熵，得到

$$  
H(X_1\mid Y_1,Y_2)\le H(X_1\mid Y_1),  
$$

  

$$  
H(X_2\mid Y_1,Y_2)\le H(X_2\mid Y_2).  
$$

  

因此

$$  
H(X_1,X_2\mid Y_1,Y_2) \le H(X_1\mid Y_1)+H(X_2\mid Y_2).  
$$

  

^eq-2-1-10

#### 等号条件

要使最终不等式取等，推导链中的每一步都必须取等：

1. $X_1$ 与 $X_2$ 在给定 $(Y_1,Y_2)$ 后条件独立；
    
2. $X_1$ 与 $Y_2$ 在给定 $Y_1$ 后条件独立；
    
3. $X_2$ 与 $Y_1$ 在给定 $Y_2$ 后条件独立。
    

分别写成：

$$  
P_{X_1,X_2\mid Y_1,Y_2} = P_{X_1\mid Y_1,Y_2}P_{X_2\mid Y_1,Y_2},  
$$

  

$$  
P_{X_1\mid Y_1,Y_2}=P_{X_1\mid Y_1},  
$$

  

$$  
P_{X_2\mid Y_1,Y_2}=P_{X_2\mid Y_2}.  
$$

  

合并可得

$$  
P_{X_1,X_2\mid Y_1,Y_2} = P_{X_1\mid Y_1}P_{X_2\mid Y_2}.  
$$

  

---

## 核心公式总表

|教材编号/索引|概念|公式|含义|
|---|---|---|---|
|[[#^thm-2-1|Theorem 2.1]]|自信息|$I(p)=-c\log_bp$|
|[[#^def-2-2|Definition 2.2]]|熵|$H(X)=-\sum_xP_X(x)\log_2P_X(x)$|
|[[#^ex-2-3|Example 2.3]]|二元熵|$h_b(p)=-p\log_2p-(1-p)\log_2(1-p)$|
|[[#^def-2-8|Definition 2.8]]|联合熵|$H(X,Y)=-\sum_{x,y}P_{X,Y}(x,y)\log_2P_{X,Y}(x,y)$|
|[[#^def-2-9|Definition 2.9]]|条件熵|$H(Y\mid X)=-\sum_{x,y}P_{X,Y}(x,y)\log_2P_{Y\mid X}(y\mid x)$|
|[[#^thm-2-10|Theorem 2.10]]|链式法则|$H(X,Y)=H(X)+H(Y\mid X)$|
|[[#^lem-2-12|Lemma 2.12]]|条件化不增熵|$H(X\mid Y)\le H(X)$|
|[[#^lem-2-13|Lemma 2.13]]|独立时可加|$H(X,Y)=H(X)+H(Y)$|
|[[#^lem-2-14|Lemma 2.14]]|条件熵次可加|$H(X_1,X_2\mid Y_1,Y_2)\le H(X_1\mid Y_1)+H(X_2\mid Y_2)$|

---

## 直观理解

### 自信息为什么是负对数？

独立事件同时发生时，概率相乘：

$$  
p_1p_2.  
$$

  

而我们希望信息量相加。负对数恰好把乘法转化为加法：

$$  
-\log(p_1p_2)=-\log p_1-\log p_2.  
$$

  

### 熵为什么在均匀分布时最大？

均匀分布中，所有结果都同样可能，没有任何结果可以被优先预测，因此不确定性最大。

### 为什么条件化会降低熵？

不知道 $Y$ 时，$X$ 的边缘分布是多个条件分布 $P_{X\mid Y=y}$ 的混合。混合会掩盖不同条件分布之间的差异，使整体通常更难预测，因此

$$  
H(X)\ge H(X\mid Y).  
$$

  

### 为什么相关变量的联合熵小于熵之和？

若 $X$ 和 $Y$ 相关，知道 $X$ 后可以部分预测 $Y$。分别编码 $X$ 和 $Y$ 会重复计算一部分共享信息，因此

$$  
H(X,Y)\le H(X)+H(Y).  
$$

  

---

## 易错点总结

> [!danger] 易错点 1：把 $c$ 当作对数函数 $c$ 是正的数值常数，不是 $\log_2$。以 bit 为单位时，取 $b=2,c=1$。

> [!danger] 易错点 2：忽略 $p=0$ 时自信息发散 $I(0)=+\infty$，所以自信息函数严格的实值定义域应为 $(0,1]$。

> [!danger] 易错点 3：把平均不等式理解为逐点不等式 $H(X\mid Y)\le H(X)$ 是对 $Y$ 平均后的结论。某个具体的 $y$ 可能满足 $H(X\mid Y=y)>H(X)$。

> [!danger] 易错点 4：把条件熵写成普通熵 条件熵必须先对每个条件分布求熵，再对条件变量取平均：
> 
> $$  
> H(Y\mid X)=\sum_xP_X(x)H(Y\mid X=x).  
> $$
> 
>   

> [!danger] 易错点 5：Log-sum 的等号条件忽略零概率项 更严谨的说法是：在有效支撑上 $a_i/b_i$ 必须为常数，并且不能存在 $a_i>0,b_i=0$ 的项。

> [!danger] 易错点 6：把“熵最大”当作 Log-sum 的证明 Log-sum 的标准证明来自 $t\log t$ 的凸性与 Jensen 不等式，而不是直接来自均匀分布熵最大。

---

## 后续知识连接

- [[Kullback–Leibler 散度]]
    
- [[互信息]]
    
- [[交叉熵]]
    
- [[Jensen 不等式]]
    
- [[熵的凹性]]
    
- [[相对熵的非负性]]
    
- [[数据处理不等式]]
    
- [[典型集与渐近等分性质]]
    
- [[信道容量]]
    

---

## 一句话总结

> 自信息用 $-\log p$ 衡量单个事件的惊讶程度；熵是自信息的期望；联合熵遵循链式法则；额外条件平均不会增加不确定性；独立性恰好对应联合熵的完全可加。