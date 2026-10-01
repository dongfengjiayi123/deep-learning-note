# 第 2 章 · 定理 2.14(Riesz 表示定理)翻译与解读

> 出处:Rudin, *Real and Complex Analysis*, 3rd ed., Theorem 2.14, pp. 40–47。
> 本笔记对应书中 "POSITIVE BOREL MEASURES" 一节。

---

## 0. 一句话概括

**局部紧 Hausdorff 空间上,紧支撑连续函数空间 $\mathcal{C}_c(X)$ 上的每个正线性泛函 $\Lambda$,都恰好是"对某个正则 Borel 测度 $\mu$ 的积分"。**

即:泛函 $\Lambda f = \int_X f\,d\mu$。换句话说,积分这个"算子"完全由它背后的测度决定,反过来测度也完全由它诱导的积分泛函决定——**正线性泛函 ⟷ 正则 Borel 测度,一一对应**。

---

## 1. 记号澄清(原书扫描件 / OCR 常见乱码对照)

| 真实记号                | 含义                                                          |
| ------------------- | ----------------------------------------------------------- |
| $\mathfrak{M}$      | 定理构造出的 $\sigma$-代数                                          |
| $\mathfrak{M}_F$    | 有限测度且内正则的集合类                                                |
| $\mu$               | 构造出的测度                                                      |
| $\Lambda$           | 正线性泛函                                                       |
| $\sigma$-algebra    | $\sigma$-代数                                                 |
| $K \prec f \prec V$ | $0\le f\le 1$,$f=1$ 于 $K$ 上,$\operatorname{supp}f\subset V$ |
| $\Lambda f$         | 泛函作用                                                        |
| $2^{-i}\varepsilon$ | 二分之一的 $i$ 次幂乘 $\varepsilon$                                 |

---

## 2. 定理陈述(翻译)

设 $X$ 是**局部紧 Hausdorff** 空间,$\Lambda$ 是 $\mathcal{C}_c(X)$ 上的**正线性泛函**。则:

- 存在 $X$ 中的 $\sigma$-代数 $\mathfrak{M}$,它包含 $X$ 的一切 Borel 集;
- 存在 $\mathfrak{M}$ 上**唯一**的正测度 $\mu$,使得

**(a)(表示性质)** 对一切 $f\in\mathcal{C}_c(X)$:
$$
\Lambda f = \int_X f\,d\mu .
$$

且 $\mu$ 还具有以下性质:

**(b) 有限性** 对每个紧集 $K\subset X$:$\mu(K)<\infty$。

**(c) 外正则性** 对每个 $E\in\mathfrak{M}$:
$$
\mu(E) = \inf\{\mu(V): E\subset V,\ V\text{ 开}\}.
$$

**(d) 内正则性** 对每个**开集** $E$,以及对每个满足 $\mu(E)<\infty$ 的 $E\in\mathfrak{M}$:
$$
\mu(E) = \sup\{\mu(K): K\subset E,\ K\text{ 紧}\}.
$$

**(e) 完备性** 若 $E\in\mathfrak{M}$,$A\subset E$,$\mu(E)=0$,则 $A\in\mathfrak{M}$。

**"正"的含义**:$\Lambda$ 是复向量空间 $\mathcal{C}_c(X)$ 上的线性泛函,且对每个取值于非负实数的 $f$,有 $\Lambda f\in[0,\infty)$。简言之:$f(X)\subset[0,\infty)\implies \Lambda f\in[0,\infty)$。

> 注:$\mathfrak{M}$ 不一定是 Borel $\sigma$-代数本身,而是它的**完备化**(比 Borel 集多一点零测集)。书中 Thm 2.18 说明:在 $\sigma$-紧等"reasonable"空间上,满足 (b) 的 Borel 测度自动满足 (c)(d),且 (d) 对一切 $E\in\mathfrak{M}$ 成立。

---

## 3. 前置工具

- **Urysohn 引理(Thm 2.12)**:$X$ 局部紧 Hausdorff,$K\subset V$,$K$ 紧 $V$ 开 $\implies$ 存在 $f\in\mathcal{C}_c(X)$ 使 $K\prec f\prec V$。
- **单位分解(Thm 2.13)**:若 $K$ 紧且 $K\subset V_1\cup\cdots\cup V_n$($V_i$ 开),则存在 $h_i\prec V_i$ 使得在 $K$ 上 $\sum_i h_i(x)=1$,且每个 $h_i$ 取值于 $[0,1]$。
- **记号(只用于实值函数!)**:$f\prec V$ 表示 $f$ 是**实值**连续函数,$0\le f\le 1$,$\operatorname{supp}f\subset V$ 且紧。$K\prec f$ 表示 $f$ 实值、$0\le f\le 1$、$f\equiv 1$ 于 $K$ 上。$K\prec f\prec V$ 即两者同时成立。
  - **为什么可以写 $\mu(K)\le\Lambda f$ 这种不等式?** 因为所有出现序关系($\le$、$\sup$、$\inf$、单调性)的场合,函数都是实值的,且 $f\ge0$ 时由正性 $\Lambda f\ge0$,故 $\Lambda f$ 是非负实数。**复函数只在 Step X 最后通过线性被"搬运"过去**(见 §5 末)。
  - 线性泛函的值总是有限复数($\Lambda:\mathcal{C}_c(X)\to\mathbb{C}$),所以 $\Lambda f<+\infty$ 恒成立——这正是 (b) 能被推出来的原因。

---

## 4. 证明结构总览

证明分两大部分:

### 4.1 唯一性(先证)

思路:若 $\mu$ 满足 (c)(d),则 $\mu$ 在 $\mathfrak{M}$ 上的值**由其在紧集上的值完全决定**——任意 $E$ 先用开集从外逼近 (c),开集再用紧集从内逼近 (d)。所以只要证 $\mu_1(K)=\mu_2(K)$ 对一切紧集 $K$。

固定紧集 $K$ 与 $\varepsilon>0$:

1. 由 (b)(c),取开集 $V\supset K$ 使 $\mu_2(V)<\mu_2(K)+\varepsilon$;
2. 由 Urysohn 引理取 $f$ 使 $K\prec f\prec V$;
3. 关键不等式链($\chi_K\le f\le\chi_V$):
$$
\mu_1(K)=\int\chi_K\,d\mu_1\le\int f\,d\mu_1=\Lambda f=\int f\,d\mu_2\le\int\chi_V\,d\mu_2=\mu_2(V)<\mu_2(K)+\varepsilon .
$$
4. $\varepsilon$ 任意 $\implies \mu_1(K)\le\mu_2(K)$;交换 $\mu_1,\mu_2$ 角色得反向不等式。

**附注**:上面这串计算还顺便证明了 **(a) 蕴含 (b)**(把 $\mu_1$ 换成任意测度 $\mu$,$\mu(K)\le\Lambda f<\infty$ 若取 $f$ 满足 $K\prec f$)。——注意 (b) 其实是表示性质的推论,不是独立假设。

### 4.2 存在性(构造 $\mu$ 与 $\mathfrak{M}$)

**第一步:定义 $\mu$。**

对开集 $V$:
$$
\mu(V)=\sup\{\Lambda f: f\prec V\}. \tag{1}
$$

对任意 $E\subset X$(注意!是**所有**子集,先不管可测性):
$$
\mu(E)=\inf\{\mu(V): E\subset V,\ V\text{ 开}\}. \tag{2}
$$

> $\mu$ 一开始对 $\mathcal{P}(X)$ 全体都定义了;但可数可加性只会在 $\mathfrak{M}$ 上成立。这是"外测度风格"的定义,但 $\mu$ 不保证是外测度(次可加性 Step I 会证,但可数可加性只在 $\mathfrak{M}$ 上)。

**第二步:定义 $\mathfrak{M}_F$ 与 $\mathfrak{M}$(全书最"技术"的地方)。**

$$
E\in\mathfrak{M}_F \iff \mu(E)<\infty \ \text{ 且 }\ \mu(E)=\sup\{\mu(K): K\subset E,\ K\text{ 紧}\}. \tag{3}
$$
$$
E\in\mathfrak{M} \iff E\cap K\in\mathfrak{M}_F\ \text{ 对每个紧集 }K.
$$

**直觉**:$\mathfrak{M}_F$ = "有限测度且内正则"的集合;$\mathfrak{M}$ = "与任何紧集相交后都落入 $\mathfrak{M}_F$"的集合。为什么用紧集截断?因为 $X$ 未必 $\sigma$-紧,测度可能是"无穷大",必须逐紧集控制。等 Step VIII 会证明:$\mathfrak{M}_F$ 恰好就是 $\mathfrak{M}$ 中有限测度的集合。

### 4.3 十步证明的路线图(每步在干什么)

| 步骤       | 结论                                                                                     | 作用                                                                                                  |
| -------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **I**    | 次可加性 $\mu(\bigcup E_i)\le\sum\mu(E_i)$(任意子集)                                           | 为可数可加性铺路;证明分两步:先两个开集(用 Thm 2.13 单位分解),再用开集逼近                                                        |
| **II**   | $K$ 紧 $\implies K\in\mathfrak{M}_F$,且 $\mu(K)=\inf\{\Lambda f:K\prec f\}$              | 得 (b);并得到工具不等式 $\mu(K)\le\Lambda f$(当 $K\prec f$)                                                   |
| **III**  | 每个开集满足 (3)                                                                             | 开集(有限测度者)落入 $\mathfrak{M}_F$                                                                        |
| **IV**   | $\mathfrak{M}_F$ 中两两不交的可数并:$\mu(\bigcup E_i)=\sum\mu(E_i)$;总测度有限时并集仍在 $\mathfrak{M}_F$ | 可数可加性的核心;先证两个不交紧集的加法性 $\mu(K_1\cup K_2)=\mu(K_1)+\mu(K_2)$(用 Urysohn 造 $f$ 在 $K_1$ 上为 1、$K_2$ 上为 0) |
| **V**    | $E\in\mathfrak{M}_F$ 可被紧集与开集夹逼:存在 $K\subset E\subset V$ 且 $\mu(V-K)<\varepsilon$       | 正则性的"元定理",服务 Step VI                                                                                |
| **VI**   | $\mathfrak{M}_F$ 对差、并、交封闭                                                              | $\mathfrak{M}_F$ 是环;为 Step VII 的 $\sigma$-代数证明准备                                                    |
| **VII**  | $\mathfrak{M}$ 是 $\sigma$-代数,且包含一切 Borel 集                                             | 补集封闭用差封闭;可数并拆成不交并(递推定义 $B_n$)后用 Step IV                                                             |
| **VIII** | $\mathfrak{M}_F=\{E\in\mathfrak{M}:\mu(E)<\infty\}$                                    | 得 (d);两方向都用"夹逼 + Step V"的 $\varepsilon$ 技巧                                                          |
| **IX**   | $\mu$ 在 $\mathfrak{M}$ 上可数可加                                                           | 由 Steps IV + VIII 直接得到:$\mu$ 是测度                                                                    |
| **X**    | $\Lambda f=\int_X f\,d\mu$ 对一切 $f\in\mathcal{C}_c(X)$                                  | 得 (a);只证 $\Lambda f\le\int f\,d\mu$,再用 $\Lambda(-f)=-\Lambda f$ 得反向不等式                              |

---

## 5. 关键步骤详解

### Step I(次可加性)为什么能成立?

先对两个**开集** $V_1,V_2$ 证 $\mu(V_1\cup V_2)\le\mu(V_1)+\mu(V_2)$:取 $g\prec V_1\cup V_2$,由 Thm 2.13 存在 $h_1\prec V_1$、$h_2\prec V_2$ 且 $h_1+h_2=1$ 于 $\operatorname{supp}g$ 上。则 $h_1g\prec V_1$、$h_2g\prec V_2$,故
$$
\Lambda g=\Lambda(h_1g)+\Lambda(h_2g)\le\mu(V_1)+\mu(V_2).
$$
对一切 $g\prec V_1\cup V_2$ 取上确界即得。一般情形:若某个 $\mu(E_i)=\infty$ 平凡;否则取开集 $V_i\supset E_i$ 使 $\mu(V_i)<\mu(E_i)+2^{-i}\varepsilon$。任何 $f\prec\bigcup V_i$ 的支撑紧,故 $f\prec V_1\cup\cdots\cup V_n$(有限个),归纳用两开集情形,再令 $\varepsilon\to0$。

**要点**:紧支撑(compact support)把"无穷并"化成了"有限并"——这是 $\mathcal{C}_c(X)$ 定义的意义所在。

### Step II(紧集有限)为何 $\mu(K)\le\Lambda f$?

若 $K\prec f$,对 $0<a<1$ 令 $V_a=\{x:f(x)>a\}$,则 $K\subset V_a$ 且 $a g\le f$ 对一切 $g\prec V_a$(因为 $g$ 的支撑在 $V_a$ 内,$g\le 1$,故 $ag\le f$)。由 $\Lambda$ 单调:
$$
\mu(K)\le\mu(V_a)=\sup_{g\prec V_a}\Lambda g\le a^{-1}\Lambda f,
$$
令 $a\to1$ 得 $\mu(K)\le\Lambda f$。反向:取开集 $V\supset K$ 使 $\mu(V)<\mu(K)+\varepsilon$,由 Urysohn 得 $K\prec f\prec V$,则 $\Lambda f\le\mu(V)<\mu(K)+\varepsilon$。合起来 $\mu(K)=\inf\{\Lambda f:K\prec f\}$。

### Step IV(不交并的可加性)关键一步

先证**不交紧集** $K_1,K_2$:由 Urysohn 取 $f\in\mathcal{C}_c(X)$,$f\equiv1$ 于 $K_1$,$f\equiv0$ 于 $K_2$,$0\le f\le1$。再由 Step II 取 $g$ 使 $K_1\cup K_2\prec g$ 且 $\Lambda g<\mu(K_1\cup K_2)+\varepsilon$。则 $K_1\prec fg$、$K_2\prec(1-f)g$,于是
$$
\mu(K_1)+\mu(K_2)\le\Lambda(fg)+\Lambda(g-fg)=\Lambda g<\mu(K_1\cup K_2)+\varepsilon .
$$
反向由 Step I(次可加性)给出。这就是"测度在紧集上的加法性",再用紧集内逼近(Eq. 11 的 $2^{-i}\varepsilon$ 技巧)推广到 $\mathfrak{M}_F$ 中的集合。

### Step VII($\mathfrak{M}$ 是 $\sigma$-代数)怎么证的?

- **补集**:$A\in\mathfrak{M}\implies A^c\cap K=K-(A\cap K)$,是 $\mathfrak{M}_F$ 中两个集合之差(Step VI)⟹ $\in\mathfrak{M}_F$。
- **可数并**:$A=\bigcup A_i$,$A_i\in\mathfrak{M}$。令 $B_n=(A_n\cap K)-(B_1\cup\cdots\cup B_{n-1})$(递推地抠掉前面),则 $\{B_n\}$ 是 $\mathfrak{M}_F$ 中两两不交的序列,且 $\bigcup B_n=A\cap K$;由 Step IV,$A\cap K\in\mathfrak{M}_F$。
- **包含 Borel 集**:闭集 $C$ 满足 $C\cap K$ 紧 ⟹ $C\in\mathfrak{M}$;而 $\sigma$-代数中所有闭集 ⟹ 所有 Borel 集。

### Step X(表示性质)的核心技巧

只对**实值** $f$ 证 $\Lambda f\le\int f\,d\mu$:

1. 设 $K=\operatorname{supp}f$,$[a,b]$ 含 $f$ 的值域,取分点 $y_0<a<y_1<\cdots<y_n=b$,$y_i-y_{i-1}<\varepsilon$;
2. **分层(level sets)**:
$$
E_i=\{x:y_{i-1}<f(x)\le y_i\}\cap K\qquad(i=1,\dots,n),
$$
$E_i$ 是两两不交的 Borel 集,并起来是 $K$;
3. 取开集 $V_i\supset E_i$ 使 $\mu(V_i)<\mu(E_i)+\varepsilon/n$,且在 $V_i$ 上 $f(x)<y_i+\varepsilon$;
4. 由 Thm 2.13 取 $h_i\prec V_i$ 使 $\sum h_i=1$ 于 $K$ 上,则 $f=\sum h_i f$;
5. 逐项估计($h_if\le(y_i+\varepsilon)h_i$):
$$
\Lambda f=\sum\Lambda(h_if)\le\sum(y_i+\varepsilon)\Lambda h_i\le\sum(y_i+\varepsilon)\bigl(\mu(E_i)+\tfrac{\varepsilon}{n}\bigr)\le\int f\,d\mu+O(\varepsilon).
$$
6. $\varepsilon\to0$ 得 $\Lambda f\le\int f\,d\mu$;再以 $-f$ 代 $f$ 得反向不等式。

**思想**:用"值域分层 + 单位分解"把任意连续函数拆成"近似阶梯函数"的线性组合,把泛函 $\Lambda$ 的作用化为测度 $\mu$ 的作用。这就是 (a) 的本质:$\Lambda$ 在"台阶"上等于 $\mu$ 的积分,连续函数是台阶的一致极限。

---

## 6. 直觉、误区与后续用途

### 直觉
- "测度 = 积分泛函"互为表里:给 $\mu$ 定义 $\Lambda f=\int f\,d\mu$ 是平凡的;定理的深刻方向是**反过来**:一个抽象的"加权求和"算子 $\Lambda$,其权重必然来自某个点集上的质量分布 $\mu$。
- 定理把对偶空间 $\mathcal{C}_c(X)^*$ 与"正则 Borel 测度"等同起来。

### 常见误区
1. $\mu$ 一开始对**所有**子集都有定义,但**可数可加性只在 $\mathfrak{M}$ 上成立**——不要以为 $\mu$ 在 $\mathcal{P}(X)$ 上是测度。
2. (c) 对一切 $E\in\mathfrak{M}$ 成立,但 (d) **只**对开集与有限测度集合成立(定理陈述如此;Thm 2.18 说明在 $\sigma$-紧空间上 (d) 对一切 $E$ 成立)。
3. "正"线性泛函的"正"是**保序**:$f\ge0\implies\Lambda f\ge0$;由此自动推出 $\Lambda$ 单调($f\le g\implies\Lambda f\le\Lambda g$),这是证明中反复使用的性质(如 Step II、Step X)。
4. 唯一性是**在满足 (c)(d) 的测度中**唯一;这正是为什么定理要把 (c)(d) 写进结论。
5. $\mathfrak{M}$ 不是"某个预先给定的" $\sigma$-代数,而是**由 $\Lambda$ 自己长出来的**——构造决定了它自动完备 ((e))。

### 后续用途
- **Thm 2.20**:由此构造出 $\mathbb{R}^n$ 上的 Lebesgue 测度(用 $\Lambda f=\int_{\mathbb{R}^n}f\,dx$ 的 Riemann 积分作泛函)。
- 第 6 章:$L^p$ 对偶 $(L^p)^*\cong L^q$ 依赖 Riesz 表示。
- 第 6 章复测度、全变差;第 10 章以后 $\mathbb{T}$ 上的测度与 $H^p$ 空间、圆周上的 Fourier 分析。
- Banach 代数中 Gelfand 表示、正线性泛函(第 18 章)也以此为原型。
