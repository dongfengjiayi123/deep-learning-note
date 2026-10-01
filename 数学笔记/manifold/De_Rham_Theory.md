
---
title: De Rham Theory（§24–§29）
aliases:
  - 德拉姆理论
  - De Rham Cohomology
  - 德拉姆上同调
tags:
  - differential-geometry
  - algebraic-topology
  - differential-forms
  - cohomology
source: L. W. Tu, An Introduction to Manifolds, §24–§29
status: review
---

# De Rham Theory（§24–§29）

> [!abstract] 核心主线
> 微分形式形成上链复形
> $$
> 0\longrightarrow \Omega^0(M)\xrightarrow d\Omega^1(M)\xrightarrow d\Omega^2(M)\xrightarrow d\cdots,
> \qquad d^2=0.
> $$
> de Rham 上同调
> $$
> H^k_{\mathrm{dR}}(M)=\frac{\ker(d:\Omega^k(M)\to\Omega^{k+1}(M))}
> {\operatorname{im}(d:\Omega^{k-1}(M)\to\Omega^k(M))}
> $$
> 衡量“闭形式不一定恰当”的程度，并把流形的全局拓扑编码成向量空间乃至分次环。

## 阅读地图

- [[#§24 De Rham Cohomology]]：定义、圆周、函子性与环结构
- [[#§25 The Long Exact Sequence in Cohomology]]：上链复形、连接同态、zig-zag lemma
- [[#§26 The Mayer–Vietoris Sequence]]：用开覆盖计算上同调
- [[#§27 Homotopy Invariance]]：同伦等价空间具有相同 de Rham 上同调
- [[#§28 Computation of De Rham Cohomology]]：环面、曲面与常见例子
- [[#§29 Proof of Homotopy Invariance]]：用上链同伦证明同伦不变性

---

# §24 De Rham Cohomology

## 24.0 动机：从线积分到拓扑障碍

在 $\mathbb R^3$ 中：

- 若向量场 $F=\nabla f$，则
  $$
  \int_C F\cdot dr=f(q)-f(p),
  $$
  积分只依赖端点。
- 在微分形式语言中，$F$ 对应一个 $1$-形式 $\omega$，而 $F=\nabla f$ 对应
  $$
  \omega=df.
  $$
- 若 $\omega$ 是恰当形式，则必为闭形式，因为
  $$
  d\omega=d(df)=d^2f=0.
  $$

真正的问题是反方向：

> 闭形式 $d\omega=0$ 是否一定恰当，即是否存在 $\tau$ 使 $\omega=d\tau$？

答案取决于定义域的全局拓扑。

- 在 $\mathbb R^n$ 或更一般的可缩流形上，正次数闭形式都是恰当的。
- 在穿孔平面 $\mathbb R^2\setminus\{0\}$ 上存在闭而不恰当的 $1$-形式，例如
  $$
  \omega=\frac{-y\,dx+x\,dy}{x^2+y^2}.
  $$
  它沿单位圆的积分为 $2\pi$，因此不可能是恰当形式。

> [!note] 历史背景
> Poincaré 的工作把微分形式的局部可积性与拓扑问题联系起来；de Rham 在 1931 年的论文中建立了微分形式与拓扑上同调之间的核心对应。现代的 de Rham 定理表明，de Rham 上同调与实系数奇异上同调同构。

## 24.1 De Rham Cohomology

### 24.1.1 闭形式与恰当形式

对光滑流形 $M$，定义

$$
Z^k(M):=\ker\bigl(d:\Omega^k(M)\to\Omega^{k+1}(M)\bigr),
$$

$$
B^k(M):=\operatorname{im}\bigl(d:\Omega^{k-1}(M)\to\Omega^k(M)\bigr).
$$

其中：

- $Z^k(M)$：闭 $k$-形式空间；
- $B^k(M)$：恰当 $k$-形式空间。

由 $d^2=0$，有

$$
B^k(M)\subseteq Z^k(M).
$$

### 24.1.2 定义：de Rham 上同调

$$
\boxed{H^k(M):=Z^k(M)/B^k(M)}.
$$

闭形式 $\omega$ 的等价类记为 $[\omega]$。两个闭形式 $\omega,\omega'$ 同调，当且仅当

$$
\omega'-\omega=d\tau.
$$

也就是

$$
[\omega']=[\omega]\iff \omega'=\omega+d\tau.
$$

> [!important] 直觉
> 一个上同调类不是某个具体形式，而是“相差一个恰当形式”的所有闭形式组成的等价类。

### Proposition 24.1：零次上同调

若 $M$ 有 $r$ 个连通分支，则

$$
H^0(M)\cong \mathbb R^r.
$$

理由：$0$-形式就是光滑函数，而

$$
df=0
$$

等价于 $f$ 局部常值，因此 $f$ 在每个连通分支上为常数。

> [!warning] 易错点：无限多个连通分支
> 若连通分支集合为 $I$，则
> $$
> H^0(M)\cong \prod_{i\in I}\mathbb R,
> $$
> 即给每个连通分支任意指定一个实数。一般不是直和 $\bigoplus_{i\in I}\mathbb R$，因为不要求只有有限多个分支取非零值。

### Proposition 24.2：超过维数的上同调消失

若 $\dim M=n$，则对 $k>n$，

$$
\Omega^k(M)=0,
\qquad H^k(M)=0.
$$

原因是 $n$ 维向量空间上不存在非零的交替 $k$-线性形式（$k>n$）。

## 24.2 Examples of de Rham Cohomology

### Example 24.3：实直线 $\mathbb R$

因为 $\mathbb R$ 连通，

$$
H^0(\mathbb R)=\mathbb R.
$$

任意 $1$-形式可写为

$$
\omega=f(x)\,dx.
$$

由于 $\mathbb R$ 上没有非零 $2$-形式，所有 $1$-形式自动闭。取

$$
g(x)=\int_0^x f(t)\,dt,
$$

则

$$
dg=f(x)\,dx=\omega.
$$

所以

$$
\boxed{H^k(\mathbb R)=
\begin{cases}
\mathbb R,&k=0,\\
0,&k\ge 1.
\end{cases}}
$$

### Example 24.4：圆周 $S^1$

因为 $S^1$ 连通且一维，

$$
H^0(S^1)=\mathbb R,
\qquad H^k(S^1)=0\quad(k\ge2).
$$

在 $S^1\subset\mathbb R^2$ 上取

$$
\omega=-y\,dx+x\,dy.
$$

用参数化

$$
F(t)=(\cos t,\sin t),\qquad 0\le t\le2\pi,
$$

得到

$$
F^*\omega=dt,
$$

因此

$$
\int_{S^1}\omega=\int_0^{2\pi}dt=2\pi.
$$

定义积分映射

$$
\varphi:\Omega^1(S^1)\to\mathbb R,
\qquad
\varphi(\alpha)=\int_{S^1}\alpha.
$$

因为 $S^1$ 一维，每个 $1$-形式都闭。由 Stokes 定理，恰当形式满足

$$
\int_{S^1}dg=0,
$$

所以 $B^1(S^1)\subseteq\ker\varphi$。

反过来，若 $\int_{S^1}\alpha=0$，把 $\alpha$ 拉回到 $\mathbb R$，写成

$$
h^*\alpha=\bar f(t)\,dt,
$$

其中 $\bar f$ 为 $2\pi$-周期函数。令

$$
\bar g(t)=\int_0^t\bar f(u)\,du.
$$

零积分条件保证 $\bar g$ 也是 $2\pi$-周期函数，故下降为 $S^1$ 上的函数 $g$，并满足 $dg=\alpha$。

于是

$$
\ker\varphi=B^1(S^1),
$$

从而积分诱导同构

$$
\boxed{H^1(S^1)\xrightarrow{\sim}\mathbb R,
\qquad [\alpha]\mapsto\int_{S^1}\alpha.}
$$

综上：

$$
\boxed{H^k(S^1)=
\begin{cases}
\mathbb R,&k=0,1,\\
0,&\text{其他}.
\end{cases}}
$$

> [!danger] 原文/OCR 易错点
> 1. 应为 $\varphi(\omega)=2\pi\neq0$，不是 $2\pi=0$。
> 2. “积分为零推出恰当”依赖于圆周上的周期原函数构造，不能直接由 Stokes 定理反推。
> 3. $h^*:\Omega^1(S^1)\to\Omega^1(\mathbb R)$ 的单射性来自覆盖映射/局部微分同胚的性质。

## 24.3 Diffeomorphism Invariance

若 $F:N\to M$ 光滑，则拉回

$$
F^*:\Omega^k(M)\to\Omega^k(N)
$$

满足

$$
dF^*=F^*d.
$$

因此：

- 闭形式被拉回为闭形式；
- 恰当形式被拉回为恰当形式。

故 $F^*$ 诱导上同调映射

$$
F^*:H^k(M)\to H^k(N),
\qquad
F^*[\omega]=[F^*\omega].
$$

注意方向反转：

$$
F:N\to M
\quad\Longrightarrow\quad
F^*:H^k(M)\to H^k(N).
$$

函子性：

$$
(\operatorname{id}_M)^*=\operatorname{id}_{H^k(M)},
$$

$$
(G\circ F)^*=F^*\circ G^*.
$$

因此 de Rham 上同调是一个**反变函子**。若 $F$ 是微分同胚，则 $F^*$ 是同构。

> [!warning] 易错点
> 复合次序必须反过来：$(G\circ F)^*=F^*\circ G^*$。

## 24.4 The Ring Structure on de Rham Cohomology

定义

$$
[\omega]\wedge[\tau]:=[\omega\wedge\tau],
\qquad
[\omega]\in H^k(M),\ [\tau]\in H^\ell(M).
$$

需要验证：

1. 若 $\omega,\tau$ 闭，则 $\omega\wedge\tau$ 闭；
2. 改变 $\omega$ 或 $\tau$ 的代表元，只会使乘积改变一个恰当形式。

关键公式是

$$
d(\omega\wedge\tau)=d\omega\wedge\tau+(-1)^k\omega\wedge d\tau.
$$

于是

$$
H^*(M):=\bigoplus_{k=0}^{n}H^k(M)
$$

成为实数域上的分次交换代数：

$$
[\omega]\wedge[\tau]
=(-1)^{k\ell}[\tau]\wedge[\omega].
$$

特别地，若 $\deg a$ 为奇数，则

$$
a\wedge a=-a\wedge a
\quad\Longrightarrow\quad
2a^2=0.
$$

在实系数下得到

$$
a^2=0.
$$

> [!danger] 易错点
> 1. “分次交换”不等于普通交换；符号是 $(-1)^{k\ell}$。
> 2. 乘法的次数是相加：
> $$
> H^k(M)\times H^\ell(M)\to H^{k+\ell}(M).
> $$
> 3. 原 OCR 中类似 $A^{k\times\ell}$ 的写法应改为 $A^{k+\ell}$。

---

# §25 The Long Exact Sequence in Cohomology

## 25.1 Exact Sequences

### Definition 25.1：正合

序列

$$
A\xrightarrow f B\xrightarrow g C
$$

在 $B$ 处正合，指

$$
\operatorname{im}f=\ker g.
$$

短正合列是

$$
0\longrightarrow A\xrightarrow f B\xrightarrow g C\longrightarrow0.
$$

其含义：

- $f$ 单射；
- $g$ 满射；
- $\operatorname{im}f=\ker g$。

### Proposition 25.2：三项正合列

若

$$
A\xrightarrow f B\xrightarrow g C
$$

正合，则：

1. $f$ 满射 $\iff g=0$；
2. $g$ 单射 $\iff f=0$。

### Proposition 25.3：四项正合列

1. $0\to A\xrightarrow f B\to0$ 正合 $\iff f$ 是同构；
2. 若 $A\xrightarrow f B\to C\to0$ 正合，则
   $$
   C\cong\operatorname{coker}f:=B/\operatorname{im}f.
   $$

> [!warning] 编号提示
> 原文末尾习题若写成“证明 Proposition 25.1 / 25.2”，很可能是排版或 OCR 错位；对应内容应是 Proposition 25.2 与 Proposition 25.3。

## 25.2 Cohomology of Cochain Complexes

上链复形 $C=(C^k,d^k)$ 是序列

$$
\cdots\to C^{k-1}\xrightarrow{d^{k-1}}C^k\xrightarrow{d^k}C^{k+1}\to\cdots
$$

满足

$$
d^k\circ d^{k-1}=0.
$$

定义

$$
Z^k(C)=\ker d^k,
\qquad
B^k(C)=\operatorname{im}d^{k-1},
$$

$$
\boxed{H^k(C)=Z^k(C)/B^k(C).}
$$

术语：

- $k$-cochain：$C^k$ 中元素；
- $k$-cocycle：$\ker d^k$ 中元素；
- $k$-coboundary：$\operatorname{im}d^{k-1}$ 中元素。

对 de Rham 复形：

- cocycle = 闭形式；
- coboundary = 恰当形式。

### Cochain map

若 $A,B$ 是上链复形，映射 $\varphi:A\to B$ 满足

$$
d_B\circ\varphi=\varphi\circ d_A,
$$

则称为上链映射，并诱导

$$
\varphi^*:H^k(A)\to H^k(B),
\qquad
\varphi^*[a]=[\varphi(a)].
$$

## 25.3 The Connecting Homomorphism

给定短正合列

$$
0\to A\xrightarrow i B\xrightarrow j C\to0,
$$

可构造连接同态

$$
d^*:H^k(C)\to H^{k+1}(A).
$$

### Zig-zag 构造

从 $[c]\in H^k(C)$ 出发：

1. 选闭代表元 $c\in C^k$；
2. 因 $j:B^k\to C^k$ 满射，选 $b\in B^k$ 使
   $$
   j(b)=c;
   $$
3. 因 $dc=0$ 且 $jd=dj$，有
   $$
   j(db)=d(jb)=dc=0;
   $$
4. 由正合性 $\ker j=\operatorname{im}i$，存在唯一 $a\in A^{k+1}$ 使
   $$
   i(a)=db;
   $$
5. 可证明 $da=0$，定义
   $$
   d^*[c]=[a].
   $$

示意：

```text
A^{k+1} --i--> B^{k+1}
   a            db
                ↑d
A^k     --i-->  b --j--> c ∈ C^k
