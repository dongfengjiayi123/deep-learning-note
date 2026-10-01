---
title: 2.3 多随机变量下的熵与互信息性质
aliases:
  - Properties of Entropy and Mutual Information for Multiple Random Variables
  - 多变量熵链式法则
  - 多变量互信息
created: 2026-07-28
updated: 2026-07-28
tags:
  - 信息论
  - 熵
  - 条件熵
  - 互信息
  - 链式法则
  - 独立性
  - 概率论
status: 整理完成
chapter: 2.3
source_numbering: 原教材编号
source:
  - An Introduction to Single-User Information Theory Fady Alajaji, Po-Ning Chen
---

# 2.3 多随机变量下的熵与互信息性质

> [!abstract] 本节主线
>
> 本节将前面两个变量的熵与互信息关系推广到多个随机变量：
>
> - 多变量熵的链式法则；
> - 多变量条件熵链式法则；
> - 多变量互信息链式法则；
> - 独立性导致熵最大化；
> - 条件独立情况下互信息的上界。
>
> 这些性质是后续：
>
> - 数据处理不等式；
> - 马尔可夫链；
> - 信道容量；
> - 多用户信息论
>
> 的基础。

---

# 索引导航

## 按教材编号索引


- [[#^thm-2-17|Theorem 2.17：熵的链式法则（Chain Rule for Entropy）]]

- [[#^thm-2-18|Theorem 2.18：条件熵链式法则]]

- [[#^thm-2-19|Theorem 2.19：互信息链式法则]]

- [[#^thm-2-20|Theorem 2.20：熵的独立性上界]]

- [[#^thm-2-21|Theorem 2.21：互信息上界]]

---

## 知识主题索引


- [[#2.3.1 多变量熵链式法则|Entropy Chain Rule]]

- [[#2.3.2 多变量条件熵链式法则|Conditional Entropy Chain Rule]]

- [[#2.3.3 多变量互信息链式法则|Mutual Information Chain Rule]]

- [[#2.3.4 独立变量的熵界|Independence Bound]]

- [[#2.3.5 条件独立下互信息界|Mutual Information Bound]]

- [[#核心公式总表|核心公式]]

- [[#易错点总结|易错点]]

---

# 2.3.1 多变量熵链式法则


上一节：

[[信息论_自信息与熵_Obsidian笔记#^thm-2-10|Theorem 2.10]]

给出两个随机变量：

$$
H(X,Y)=H(X)+H(Y|X)
$$


对于多个随机变量：

$$
X_1,X_2,\dots,X_n
$$


可以递归展开。


---

# Theorem 2.17：熵的链式法则


> [!theorem] Theorem 2.17（Chain Rule for Entropy）
>
> 设：
>
> $$
> X^n=(X_1,X_2,\dots,X_n)
> $$
>
> 则：
>
> $$
> \boxed{
> H(X_1,X_2,\dots,X_n)
> =
> \sum_{i=1}^{n}
> H(X_i|X_1,\dots,X_{i-1})
> }
> $$
>
> 其中：
>
> 当 $i=1$ 时：
>
> $$
> H(X_1|X_0)=H(X_1)
> $$

^thm-2-17


---

## Proof


由两变量链式法则：


$$
H(X,Y)=H(X)+H(Y|X)
$$


令：

$$
X=X_1
$$

$$
Y=(X_2,\dots,X_n)
$$


得到：

$$
H(X_1,\dots,X_n)
=
H(X_1)
+
H(X_2,\dots,X_n|X_1)
$$


继续展开第二项：

$$
H(X_2,\dots,X_n|X_1)
=
H(X_2|X_1)
+
H(X_3,\dots,X_n|X_1,X_2)
$$


不断递归：

最终得到：


$$
H(X^n)
=
\sum_{i=1}^{n}
H(X_i|X^{i-1})
$$


---

# 直观理解


多变量联合熵：

$$
H(X_1,X_2,\dots,X_n)
$$


表示：

> 同时描述所有变量需要的信息量。


链式法则表示：

可以按照顺序编码：

1. 第一个变量：

$$
H(X_1)
$$


2. 已知第一个变量后：

$$
H(X_2|X_1)
$$


3. 已知前两个变量：

$$
H(X_3|X_1,X_2)
$$


...


所以：

$$
\text{总信息量}
=
\text{逐步增加的信息量}
$$


---

# 2.3.2 条件熵链式法则


如果已经知道额外变量：

$$
Y
$$


则所有熵都在条件 $Y$ 下展开。


---

# Theorem 2.18：条件熵链式法则


> [!theorem] Theorem 2.18（Chain Rule for Conditional Entropy）
>
> 对随机变量：
>
> $$
> X_1,\dots,X_n,Y
> $$
>
> 有：
>
> $$
> \boxed{
> H(X_1,\dots,X_n|Y)
> =
> \sum_{i=1}^{n}
> H(X_i|X_1,\dots,X_{i-1},Y)
> }
> $$

^thm-2-18


---

## Proof 思路


直接将：

[[信息论_自信息与熵_Obsidian笔记#^cor-2-11|条件熵链式法则]]


递归推广即可。


对于两个变量：

$$
H(X_1,X_2|Y)
=
H(X_1|Y)
+
H(X_2|X_1,Y)
$$


继续展开即可。


---

# 2.3.3 多变量互信息


对于随机向量：

$$
X^n=(X_1,\dots,X_n)
$$


和：

$$
Y^m=(Y_1,\dots,Y_m)
$$


定义：

$$
I(X^n;Y^m)
$$


表示：

两个随机向量之间共享的信息。


---

定义：


$$
\boxed{
I(X_1,\dots,X_n;
Y_1,\dots,Y_m)
=
H(X_1,\dots,X_n)
-
H(X_1,\dots,X_n|Y_1,\dots,Y_m)
}
$$


---

# Theorem 2.19：互信息链式法则


> [!theorem] Theorem 2.19（Chain Rule for Mutual Information）
>
> 对：
>
> $$
> X_1,\dots,X_n
> $$
>
> 和：
>
> $$
> Y
> $$
>
> 有：
>
>
> $$
> \boxed{
> I(X_1,\dots,X_n;Y)
> =
> \sum_{i=1}^{n}
> I(X_i;Y|X_1,\dots,X_{i-1})
> }
> $$
>
> 当 $i=1$：
>
> $$
> I(X_1;Y|X_0)=I(X_1;Y)
> $$

^thm-2-19


---

## Proof


由互信息定义：


$$
I(X^n;Y)
=
H(X^n)-H(X^n|Y)
$$


利用 Theorem 2.17：


$$
H(X^n)
=
\sum_iH(X_i|X^{i-1})
$$


利用 Theorem 2.18：


$$
H(X^n|Y)
=
\sum_iH(X_i|X^{i-1},Y)
$$


相减：


$$
\begin{aligned}
I(X^n;Y)
&=
\sum_i
[
H(X_i|X^{i-1})
-
H(X_i|X^{i-1},Y)
]
\\
&=
\sum_i
I(X_i;Y|X^{i-1})
\end{aligned}
$$


证毕。


---

# 直观理解


整体信息：

$$
I(X_1,X_2,\dots,X_n;Y)
$$


可以拆成：

\[
\begin{aligned}
&
X_1
\text{提供的信息}
\\
+
&
X_2
\text{在知道}X_1\text{后的新增信息}
\\
+
&
X_3
\text{在知道前面变量后的新增信息}
\\
+\cdots
\end{aligned}
\]


即：

> 信息具有增量分解性质。

# 2.3.4 独立性与熵的上界


前面得到：

$$
H(X,Y)\le H(X)+H(Y)
$$


其中：

$$
H(X,Y)=H(X)+H(Y|X)
$$


由于：

$$
H(Y|X)\le H(Y)
$$


因此：

$$
H(X,Y)\le H(X)+H(Y)
$$


本节推广到多个随机变量。

---

# Theorem 2.20：独立性条件下的熵界


> [!theorem] Theorem 2.20（Independence Bound on Entropy）
>
> 对随机变量：
>
> $$
> X_1,X_2,\dots,X_n
> $$
>
> 有：
>
> $$
> \boxed{
> H(X_1,X_2,\dots,X_n)
> \le
> \sum_{i=1}^{n}H(X_i)
> }
> $$
>
> 等号成立当且仅当：
>
> $$
> X_1,X_2,\dots,X_n
> $$
>
> 相互独立。


^thm-2-20


---

## Proof


由 Theorem 2.17：

$$
H(X_1,\dots,X_n)
=
\sum_{i=1}^{n}
H(X_i|X_1,\dots,X_{i-1})
$$


由条件化不增加熵：

[[信息论_自信息与熵_Obsidian笔记#^lem-2-12|Lemma 2.12]]

有：

$$
H(X_i|X_1,\dots,X_{i-1})
\le
H(X_i)
$$


因此：

$$
\begin{aligned}
H(X_1,\dots,X_n)
&=
\sum_i
H(X_i|X_1,\dots,X_{i-1})
\\
&\le
\sum_iH(X_i)
\end{aligned}
$$


---

## 等号条件


若：

$$
H(X_i|X_1,\dots,X_{i-1})
=
H(X_i)
$$


则：

$$
X_i
\perp
(X_1,\dots,X_{i-1})
$$


对于所有：

$$
i=2,\dots,n
$$


成立。


因此：

$$
X_1,X_2,\dots,X_n
$$


相互独立。


---

# 直观理解


如果变量之间存在相关性：

例如：

$$
X_2
$$


可以由：

$$
X_1
$$

部分预测。


那么联合描述时：

不需要重复描述全部信息。


所以：

$$
H(X_1,X_2)
<
H(X_1)+H(X_2)
$$


只有完全独立：

每个变量提供新的信息：

$$
H(X_1,\dots,X_n)
=
\sum_iH(X_i)
$$


---

# 2.3.5 条件独立与互信息界


本节考虑随机过程：

$$
(X_i,Y_i),i=1,\dots,n
$$


满足条件独立：


$$
P_{Y^n|X^n}
=
\prod_{i=1}^{n}
P_{Y_i|X_i}
$$


即：

给定输入序列：

$$
X_1,\dots,X_n
$$


输出：

$$
Y_1,\dots,Y_n
$$


之间条件独立。


这对应信息论中的：

> 独立信道（memoryless channel）


---

# Theorem 2.21：互信息上界


> [!theorem] Theorem 2.21（Bound on Mutual Information）
>
> 若：
>
> $$
> P_{Y^n|X^n}
> =
> \prod_{i=1}^{n}P_{Y_i|X_i}
> $$
>
> 则：
>
> $$
> \boxed{
> I(X_1,\dots,X_n;Y_1,\dots,Y_n)
> \le
> \sum_{i=1}^{n}
> I(X_i;Y_i)
> }
> $$
>
>
> 等号成立当且仅当：
>
> $$
> X_1,X_2,\dots,X_n
> $$
>
> 相互独立。


^thm-2-21


---

# Proof


由互信息定义：


$$
I(X^n;Y^n)
=
H(Y^n)-H(Y^n|X^n)
$$


---

## 第一步：限制联合熵


由 Theorem 2.20：


$$
H(Y_1,\dots,Y_n)
\le
\sum_iH(Y_i)
$$


因此：

$$
H(Y^n)
\le
\sum_iH(Y_i)
$$


---

## 第二步：利用条件独立


条件独立：

$$
P_{Y^n|X^n}
=
\prod_iP_{Y_i|X_i}
$$


取负对数：


$$
-\log
P_{Y^n|X^n}(Y^n|X^n)
$$


得到：


$$
-\log
\prod_iP_{Y_i|X_i}(Y_i|X_i)
$$


利用：

$$
\log ab=\log a+\log b
$$


得到：


$$
=
-\sum_i
\log P_{Y_i|X_i}(Y_i|X_i)
$$


取期望：

$$
H(Y^n|X^n)
=
\sum_iH(Y_i|X_i)
$$


---

## 第三步：代入互信息


因此：

\[
\begin{aligned}
I(X^n;Y^n)
&=
H(Y^n)-H(Y^n|X^n)
\\
&\le
\sum_iH(Y_i)
-
\sum_iH(Y_i|X_i)
\\
&=
\sum_i
I(X_i;Y_i)
\end{aligned}
\]


得到：

$$
\boxed{
I(X^n;Y^n)
\le
\sum_iI(X_i;Y_i)
}
$$


---

# 等号条件


第一个不等式：

$$
H(Y^n)
\le
\sum_iH(Y_i)
$$


等号要求：

$$
Y_1,\dots,Y_n
$$


独立。


由于：

$$
X_i\rightarrow Y_i
$$

经过独立信道。


因此：

$$
Y_i
$$

独立等价于：

$$
X_i
$$

独立。


所以：

等号成立：

$$
\iff
X_1,\dots,X_n
\text{独立}
$$


---

# 直观解释：独立信道的信息不能超过单次信息之和


考虑：

$$
n
$$

次独立信道传输。


总输入：

$$
X^n
$$


总输出：

$$
Y^n
$$


如果输入之间独立：

每一次传输贡献：

$$
I(X_i;Y_i)
$$


所以：

$$
I(X^n;Y^n)
=
\sum_iI(X_i;Y_i)
$$


如果输入相关：

不同信道之间存在冗余信息：

因此：

$$
I(X^n;Y^n)
<
\sum_iI(X_i;Y_i)
$$


---

# 核心公式总表


|教材编号|名称|公式|意义|
|-|-|-|-|
|[[#^thm-2-17|Theorem 2.17]]|熵链式法则|$H(X^n)=\sum_iH(X_i|X^{i-1})$|联合熵分解|
|[[#^thm-2-18|Theorem 2.18]]|条件熵链式法则|$H(X^n|Y)=\sum_iH(X_i|X^{i-1},Y)$|条件情况下展开|
|[[#^thm-2-19|Theorem 2.19]]|互信息链式法则|$I(X^n;Y)=\sum_iI(X_i;Y|X^{i-1})$|信息增量分解|
|[[#^thm-2-20|Theorem 2.20]]|独立性熵界|$H(X^n)\le\sum_iH(X_i)$|独立时取等|
|[[#^thm-2-21|Theorem 2.21]]|互信息界|$I(X^n;Y^n)\le\sum_iI(X_i;Y_i)$|独立信道性质|

---

# 知识结构总结


## 熵方向


$$
H(X^n)
$$


通过链式法则：


$$
=
\sum_iH(X_i|X^{i-1})
$$


由于：

$$
H(X_i|X^{i-1})
\le H(X_i)
$$


得到：

$$
H(X^n)
\le
\sum_iH(X_i)
$$


---

## 互信息方向


$$
I(X^n;Y)
$$


展开：


$$
=
\sum_iI(X_i;Y|X^{i-1})
$$


---

## 独立信道方向


如果：

$$
P_{Y^n|X^n}
=
\prod_iP_{Y_i|X_i}
$$


则：

$$
I(X^n;Y^n)
\le
\sum_iI(X_i;Y_i)
$$


---

# 易错点总结


> [!danger] 易错点1：链式法则不是简单求和


错误：

$$
H(X,Y,Z)
=
H(X)+H(Y)+H(Z)
$$


只有独立时成立。


正确：


$$
H(X,Y,Z)
=
H(X)
+
H(Y|X)
+
H(Z|X,Y)
$$


---

> [!danger] 易错点2：条件熵中的条件不能丢


错误：

$$
H(X_3|X_1,X_2)
=
H(X_3)
$$


除非：

$$
X_3
\perp
(X_1,X_2)
$$


---

> [!danger] 易错点3：Theorem 2.20 的等号条件是完全独立


不是：

“两两独立”。


需要：

$$
P_{X_1,\dots,X_n}
=
\prod_iP_{X_i}
$$


---

> [!danger] 易错点4：Theorem 2.21 需要 memoryless 条件


即：

$$
P_{Y^n|X^n}
=
\prod_iP_{Y_i|X_i}
$$


否则：

$$
H(Y^n|X^n)
=
\sum_iH(Y_i|X_i)
$$


不一定成立。


---

# 后续知识连接


- [[信息论_互信息与条件互信息]]
- [[Kullback–Leibler散度]]
- [[数据处理不等式]]
- [[马尔可夫链]]
- [[Fano不等式]]
- [[信道容量]]
- [[离散无记忆信道]]
- [[随机编码]]
- [[典型集与渐近等分性质]]

---

# 一句话总结


> 多变量信息论的核心是链式分解：联合熵可以拆成逐步增加的不确定性，互信息可以拆成逐步增加的信息贡献；独立性使这种分解达到最大值，而独立信道限制了总信息不能超过单次信息之和。