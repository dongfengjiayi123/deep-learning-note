这段包含 Fano 不等式的几何解释、经典证明、等号条件以及利用数据处理不等式的另一种证明。先纠正两处扫描错误：

[  
P_e=\Pr[\hat X\neq X],  
]

错误指示变量应定义为

[  
E=  
\begin{cases}  
0,&g(Y)=X,\  
1,&g(Y)\neq X.  
\end{cases}  
]

---

# 一、Fano 不等式的核心含义

[  
\boxed{  
H(X|Y)\le h_b(P_e)+P_e\log_2(|\mathcal X|-1)  
}  
]

其中 (\hat X=g(Y))，(P_e=\Pr(\hat X\neq X))。

它说明：

> 如果观察 (Y) 后对 (X) 仍然有较大的不确定性，那么任何基于 (Y) 的估计器都不可能有很小的错误率。

右边可以分成两部分：

[  
h_b(P_e)  
]

表示“是否出错”本身的不确定性；

[  
P_e\log_2(|\mathcal X|-1)  
]

表示一旦知道发生了错误，真实 (X) 在剩余 (|\mathcal X|-1) 个候选值中的不确定性。

---

# 二、图 2.4 为什么有时既有下界又有上界？

定义

[  
f(p)=h_b(p)+p\log_2(|\mathcal X|-1).  
]

Fano 不等式就是

[  
H(X|Y)\le f(P_e).  
]

函数 (f) 的几个关键值是

[  
f(0)=0,  
]

[  
f(1)=\log_2(|\mathcal X|-1),  
]

并且它在

[  
p=\frac{|\mathcal X|-1}{|\mathcal X|}  
]

达到最大值

[  
f\left(\frac{|\mathcal X|-1}{|\mathcal X|}\right)  
=\log_2|\mathcal X|.  
]

因此 (f) 不是在整个 ([0,1]) 上单调递增，而是先增加、达到最高点后再下降。

## 情况 1

如果

[  
\log_2(|\mathcal X|-1)<H(X|Y)\le\log_2|\mathcal X|,  
]

水平线 (H(X|Y)) 会与 (f(p)) 相交两次。因此可行的 (P_e) 位于两个交点之间，既有下界，也有上界。

## 情况 2

如果

[  
0<H(X|Y)\le\log_2(|\mathcal X|-1),  
]

因为

[  
f(1)=\log_2(|\mathcal X|-1)\ge H(X|Y),  
]

所以 (P_e=1) 仍可能满足不等式，不能得到严格小于 (1) 的上界，只能得到下界。

最重要的结论是：

[  
H(X|Y)>0  
\quad\Longrightarrow\quad  
P_e\text{ 不能任意接近 }0.  
]

---

# 三、较弱但常用的版本

由于二元熵满足

[  
h_b(P_e)\le1,  
]

所以

[  
H(X|Y)  
\le  
1+P_e\log_2(|\mathcal X|-1).  
]

整理得到

[  
\boxed{  
P_e\ge  
\frac{H(X|Y)-1}  
{\log_2(|\mathcal X|-1)}  
}  
\qquad(|\mathcal X|>2).  
]

这个界比较弱，因为用 (1) 粗略替代了真实的 (h_b(P_e))。

另外，当 (H(X|Y)<1) 时，右边可能是负数；由于错误率本来满足 (P_e\ge0)，此时该简化界没有提供有效信息。更完整地可以写成

[  
P_e\ge  
\max\left{  
0,,  
\frac{H(X|Y)-1}{\log_2(|\mathcal X|-1)}  
\right}.  
]

---

# 四、经典证明的逻辑

定义错误指示变量

[  
E=\mathbf 1{\hat X\neq X}.  
]

由条件熵的链式法则，

# [  
H(E,X|Y)

H(X|Y)+H(E|X,Y),  
]

同时

# [  
H(E,X|Y)

H(E|Y)+H(X|E,Y).  
]

由于 (E) 由 (X,Y) 唯一确定，

[  
H(E|X,Y)=0.  
]

因此

# [  
H(X|Y)

H(E|Y)+H(X|E,Y).  
]

第一项满足

[  
H(E|Y)\le H(E)=h_b(P_e).  
]

第二项按 (E) 展开：

# [  
H(X|E,Y)

(1-P_e)H(X|Y,E=0)  
+  
P_eH(X|Y,E=1).  
]

当 (E=0) 时，

[  
X=g(Y),  
]

所以

[  
H(X|Y,E=0)=0.  
]

当 (E=1) 时，已知 (Y) 就已知估计值 (g(Y))，而真实 (X) 不能等于这个估计值，因此最多还有

[  
|\mathcal X|-1  
]

种可能：

[  
H(X|Y,E=1)  
\le  
\log_2(|\mathcal X|-1).  
]

所以

[  
H(X|E,Y)  
\le  
P_e\log_2(|\mathcal X|-1).  
]

合并即得

[  
H(X|Y)  
\le  
h_b(P_e)+P_e\log_2(|\mathcal X|-1).  
]

---

# 五、什么时候取等号？

经典证明中用了两个不等式：

[  
H(E|Y)\le H(E),  
]

以及

[  
H(X|Y,E=1)  
\le\log_2(|\mathcal X|-1).  
]

因此等号成立需要这两个不等式都取等号。

## 条件 1：错误事件与 (Y) 独立

[  
H(E|Y)=H(E)  
]

当且仅当

[  
E\perp Y.  
]

也就是说，对每个观测值 (y)，估计器出错的概率都相同：

[  
\Pr(E=1|Y=y)=P_e.  
]

## 条件 2：出错时均匀分布

对每个 (y)，在知道估计错误后，真实值 (X) 必须在

[  
\mathcal X\setminus{g(y)}  
]

上均匀分布：

# [  
P_{X|Y,E}(x|y,1)

\frac1{|\mathcal X|-1},  
\qquad x\neq g(y).  
]

这样其条件熵才达到最大值

[  
\log_2(|\mathcal X|-1).  
]

---

# 六、例 2.28

设 (X,Y) 相互独立，并且都在

[  
{0,1,2}  
]

上均匀分布，估计器为

[  
g(y)=y.  
]

估计正确的概率是

# [  
\Pr(X=Y)

# \sum_{x=0}^2P_X(x)P_Y(x)

# 3\cdot\frac13\cdot\frac13

\frac13.  
]

因此错误概率为

[  
P_e=1-\frac13=\frac23.  
]

因为 (X,Y) 独立，

[  
H(X|Y)=H(X)=\log_2 3.  
]

Fano 右边为

[  
h_b\left(\frac23\right)  
+  
\frac23\log_2(3-1).  
]

计算：

# [  
h_b\left(\frac23\right)

-\frac23\log_2\frac23  
-\frac13\log_2\frac13,  
]

所以

# [  
h_b\left(\frac23\right)+\frac23

\log_2 3.  
]

因此

# [  
H(X|Y)

h_b(P_e)+P_e\log_2(|\mathcal X|-1),  
]

这里确实达到等号，说明 Fano 不等式是 sharp 的。

---

# 七、另一种证明的第一步：数据处理不等式

因为

[  
\hat X=g(Y),  
]

所以构成马尔可夫链

[  
X\to Y\to\hat X.  
]

由数据处理不等式，

[  
I(X;Y)\ge I(X;\hat X).  
]

利用

[  
I(X;Y)=H(X)-H(X|Y),  
]

[  
I(X;\hat X)=H(X)-H(X|\hat X),  
]

消去 (H(X))，得到

[  
\boxed{  
H(X|Y)\le H(X|\hat X).  
}  
]

这很直观：(\hat X) 是 (Y) 的压缩或处理结果，所以只知道 (\hat X) 时，对 (X) 的不确定性不会小于知道完整 (Y) 时的不确定性。

因此，只需证明

[  
H(X|\hat X)  
\le  
h_b(P_e)+P_e\log_2(|\mathcal X|-1).  
]

---

# 八、复杂代数在做什么？

教材把 (H(X|\hat X)) 分成两部分：

- 对角线部分 (x=\hat x)：估计正确；
    
- 非对角线部分 (x\neq\hat x)：估计错误。
    

设

[  
P_e=\sum_{x\neq\hat x}P_{X,\hat X}(x,\hat x),  
]

[  
1-P_e=\sum_xP_{X,\hat X}(x,x).  
]

然后考察

[  
H(X|\hat X)  
-h_b(P_e)  
-P_e\log_2(|\mathcal X|-1).  
]

教材将其整理为

[  
\begin{aligned}  
&\sum_{x\neq\hat x}  
P_{X,\hat X}(x,\hat x)  
\log_2  
\frac{P_e}  
{P_{X|\hat X}(x|\hat x)(|\mathcal X|-1)}  
\  
&\quad+  
\sum_x  
P_{X,\hat X}(x,x)  
\log_2  
\frac{1-P_e}  
{P_{X|\hat X}(x|x)}.  
\end{aligned}  
]

目标是证明这个量不大于 (0)。

---

# 九、FI Lemma 如何使用？

这里使用的 FI Lemma 通常是

[  
\ln t\le t-1,\qquad t>0.  
]

换成以 2 为底：

[  
\boxed{  
\log_2t\le\log_2(e)(t-1).  
}  
]

对上面每一个对数项分别使用这个不等式。

例如

[  
\log_2  
\frac{P_e}  
{P_{X|\hat X}(x|\hat x)(|\mathcal X|-1)}  
]

被上界为

[  
\log_2(e)  
\left[  
\frac{P_e}  
{P_{X|\hat X}(x|\hat x)(|\mathcal X|-1)}  
-1  
\right].  
]

乘上联合概率后，利用

# [  
P_{X,\hat X}(x,\hat x)

P_{\hat X}(\hat x)P_{X|\hat X}(x|\hat x),  
]

条件概率项会被约掉。

非对角线上，对每个固定 (\hat x)，有 (|\mathcal X|-1) 个满足 (x\neq\hat x) 的值，因此最终产生

[  
\frac{P_e}{|\mathcal X|-1}  
\cdot(|\mathcal X|-1)  
=P_e.  
]

同时减去的联合概率总和也是 (P_e)，二者抵消。

对角线部分同理：

## [  
(1-P_e)\sum_xP_{\hat X}(x)

# \sum_xP_{X,\hat X}(x,x)

(1-P_e)-(1-P_e)  
=0.  
]

所以整个差值不大于 (0)：

[  
H(X|\hat X)  
-h_b(P_e)  
-P_e\log_2(|\mathcal X|-1)  
\le0.  
]

即

[  
H(X|\hat X)  
\le  
h_b(P_e)+P_e\log_2(|\mathcal X|-1).  
]

再结合

[  
H(X|Y)\le H(X|\hat X),  
]

得到 Fano 不等式。

---

# 十、两种证明的区别

第一种证明引入错误指示变量 (E)，直接把不确定性分解为

[  
\text{是否出错的不确定性}  
+  
\text{出错后真实值的不确定性}.  
]

它最直观，也最容易记忆。

第二种证明先利用数据处理不等式：

[  
H(X|Y)\le H(X|\hat X),  
]

再通过 FI Lemma 对条件熵作代数估计。它更复杂，但展示了三个重要思想之间的联系：

[  
\boxed{  
\text{数据处理不等式}  
+  
\text{条件分布分解}  
+  
\log t\le t-1  
}  
]

从理解和考试证明的角度，通常优先掌握第一种证明；第二种证明主要用于理解信息论中不同工具如何相互连接。