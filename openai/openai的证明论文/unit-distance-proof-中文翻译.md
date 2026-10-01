# 具有许多单位距离的平面点集

## OpenAI

### 摘要

对于有限平面点集 $P$，令 $\nu(P)$ 为 $P$ 中无序单位距离对的数目，并令 $\nu(n)$ 为所有 $n$ 点平面点集上 $\nu(P)$ 的最大值。我们证明，对于某个固定的 $\delta > 0$，存在无穷多个 $n$ 使得 $\nu(n) \ge n^{1+\delta}$。这否证了著名的单位距离猜想 [Erd46]。

该构造通过一个无限无分歧的完全实代数数域塔，该塔具有 3-幂次 Galois 群且次数递增，其中一组固定的有理素数完全分裂。在添加 $i$ 后，这些域产生高维格点，其元素在每个复嵌入下的像都具有绝对值 1。Golod–Shafarevich 理论确保了这样一个无限塔的存在，即使在使指定的 Frobenius 类平凡的商步骤之后也是如此。该构造的一个关键性质是，所有得到的判别式和类数至多在扩张次数上呈指数增长。

---

## 1 主要结果

对于有限集合 $P \subset \mathbb{R}^2$，令 $\nu(P) = \#\{\{x,y\} \subset P : |x-y| = 1\}$ 且 $\nu(n) = \max_{|P|=n} \nu(P)$。平面单位距离问题可追溯到 Erdős [Erd46]，他猜想存在一个绝对常数 $C$ 使得对所有足够大的 $n$，

$$\nu(n) \le n^{1+C/\log\log n}. \tag{1}$$

同一篇 1946 年的论文还引入了相异距离问题，后来由 Guth–Katz [GK15] 解决到对数因子。一个基本的上界是 $\nu(n) = O(n^{3/2})$：欧几里得单位距离图是无 $K_{2,3}$ 的，因为两个单位圆最多交于两点，而 Kővári–Sós–Turán 定理适用 [KST54]。目前已知的最佳上界 $\nu(n) = O(n^{4/3})$ 归功于 Spencer–Szemerédi–Trotter [SST84]；Székely 后来给出了这个关联数界的一个短的交点计数证明 [Sze97]。

将此与 $\mathbb{R}^2$ 上其他范数的相同问题进行比较是有用的，这一方向由 Brass 系统研究过 [Bra96]。如果单位球有一段平坦的线段，则可以安排二次数量的单位距离，因此有趣的赋范平面类比通常施加严格凸性或一般性条件。Székely 的交点计数论证扩展到严格凸范数，同样给出 $O(n^{4/3})$，而 Valtr 构造了一个严格凸范数使得该指数可以达到 [Sze97, Val05]。Eisenbrand–Pach–Rothvoß–Sopher 关于 Minkowski 和的凸独立子集的相关工作给出了相应的 $O(m^{2/3}n^{2/3}+m+n)$ 上界，随后 Bílka–Buchin–Fulek–Kiyomi–Okamoto–Tanigawa–Tóth 给出了匹配的下界 [EPRS08, BBF+10]；Brass–Moser–Pach 给出了更广泛的综述 [BMP05]。对于 Baire-一般范数，现在已知的行为要精确得多。Matoušek 证明了对大多数平面范数有 $O(n\log n \log\log n)$ [Mat11]。对于每个固定的 $d \ge 2$，Alon–Bucić–Sauermann 证明 $\mathbb{R}^d$ 上的一个剩余集（comeager set）的范数在每个 $n$ 点集上至多有 $\binom{d}{2} n \log_2 n$ 个单位距离 [ABS25]。随后 Greilhuber–Schildkraut–Tidor 证明了一个匹配的下界 $\bigl(\binom{d}{2} - o(1)\bigr) n \log_2 n$ 对所有 $\mathbb{R}^d$ 上的范数成立 [GST25]。这些结果为 Erdős 猜想提供了证据，在我们的工作之前该猜想被广泛认为是正确的。然而我们否证了单位距离猜想；我们的主要定理如下。

**定理 1.1.** 存在一个绝对常数 $\delta > 0$ 和无穷多个正整数 $n$，使得 $\nu(n) \ge n^{1+\delta}$。

我们注意到，[EF97] 中提出的一个类似的更强猜想涉及点集 $P \subset \mathbb{R}^2$，使得每个点 $x \in P$ 在 $P$ 中至少有 $k$ 个等距邻点，距离 $d_x$ 可能依赖于 $x$。定理 1.1 也否证了预测的界 $k \le n^{o(1)}$：沿着我们的序列，单位距离图的平均度为 $n^{\Omega(1)}$，而一个平均度至少为 $2k$ 的图包含一个最小度至少为 $k$ 的子图。

该构造可以看作是 Erdős 经典方格下界背后的算术的高维类比。在高斯整数 $\mathbb{Z}[i]$ 中，许多满足 $q \equiv 1 \pmod{4}$ 的有理素数的乘积具有许多形如 $z\bar{z}$ 的表示。几何上，这些表示给出了许多相同长度的格向量。我们的构造将 $\mathbb{Q}(i)$ 替换为 $K = L(i)$，其中 $L$ 是一个次数趋于无穷的完全实域。$K/L$ 的非平凡自同构 $c$ 扮演复共轭的角色：在 $K$ 的每个复嵌入下，$c$ 变为普通的复共轭。

证明分为算术部分和几何部分。算术部分构造域 $L$，其中一组固定的有理素数完全分裂。这些分裂素数在 $K = L(i)$ 中给出许多理想分解；经过类群鸽巢原理后，它们产生许多满足 $u c(u) = 1$ 的元素 $u \in K^\times$。在每个复嵌入下，这些元素具有绝对值 1，因此它们成为候选的单位平移。类群损失是无害的，因为这些域具有有界根判别式 $\operatorname{rd}(F) = |D_F|^{1/[F:\mathbb{Q}]}$。Minkowski 定理随后给出至多在域次数上呈指数增长的类数。

有界根判别式与指定的分裂同时获得。我们使用一个在三次循环域上的无分歧 pro-3 塔。Chebotarev 提供了有理素数，其 Frobenius 类可以在后面的每一层中变为平凡的。Shafarevich 的关系秩估计和 Golod–Shafarevich 理论使得所得的商塔保持无限。这是 Hajir–Maire 类域塔方法，在无分歧 pro-3 设置中；见注记 3.1。

第 2 节证明了几何准则：给定合适的数域和分裂素数，它通过将范数为一的元素嵌入高维 Minkowski 格中，用圆盘的乘积切割，并投影到一个复坐标上，来构造平面点集。第 3 节随后使用无分歧 pro-3 塔构造所需的域。附录 A 收集了下面使用的数域约定和引用。

### AI 使用声明

这个问题是以完全自动化的方式解决的。我们的内部模型被给予了一个 AI 编写的问题陈述，其输出被发送到一个 AI 评分流水线，该流水线表明对解的正确性有很高的置信度。正是在这一点之后，内部人类研究人员和数学家才开始仔细检查该解。在初步的 AI 辅助验证和重写之后，一份草稿被发送给外部数学家，包括几位数论专家，他们确认了证明的正确性（并且已经简化和加强了论证）。本手稿是对自主产生的解的人类编辑阐述，之后添加了参考文献、重新组织的证明和额外的解释材料。

给内部模型的原始 AI 编写的提示是：

**提示。** 令 $P \subset \mathbb{R}^2$ 为有限的不同点集。定义
$$\nu(P) = \left|\left\{\{p,q\} \in \binom{P}{2} : \|p-q\|_2 = 1\right\}\right|$$
并且，对每个整数 $n \ge 1$，$\nu(n) = \max_{\substack{P \subset \mathbb{R}^2 \\ |P| = n}} \nu(P)$。
完全解决 Erdős 的平面单位距离问题：$\nu(n) \le n^{1+O(1/\log\log n)}$ 当 $n \to \infty$ 时成立吗？
等价地，确定是否存在绝对常数 $C > 0$ 和 $N \in \mathbb{N}$ 使得对每个整数 $n \ge N$ 有 $\nu(n) \le n^{1+C/\log\log n}$。这里 $\log$ 表示自然对数，$N$ 可以取足够大使得 $\log\log n > 0$。$O(1/\log\log n)$ 中的隐藏常数是绝对的，与 $P$ 和 $n$ 无关。
一个完整的解必须恰好证明以下之一：
- **肯定解决。** 证明存在绝对常数 $C > 0$ 和 $N \in \mathbb{N}$ 使得每个 $n \ge N$ 个不同点的集合 $P \subset \mathbb{R}^2$ 满足 $\nu(P) \le n^{1+C/\log\log n}$。
- **否定解决。** 证明不存在这样的常数。等价地，证明对每个 $C > 0$ 和每个 $N \in \mathbb{N}$，存在一个整数 $n \ge N$ 和一个 $n$ 个不同点的集合 $P \subset \mathbb{R}^2$ 使得 $\nu(P) > n^{1+C/\log\log n}$。
对是无序的，距离是 $\mathbb{R}^2$ 中通常的欧几里得距离，渐近断言是对所有足够大的整数 $n$ 成立，而不仅仅是无穷多个 $n$。
部分进展不算，除非它蕴含上述两个解决之一。特别地，改进的界如 $O(n^{4/3-\varepsilon})$、$n^{4/3}$ 界中更好的常数、有限验证、特例、结构简化或启发式证据都是不够的，除非它们证明了完整的 Erdős 界或否证了它。

我们强调，提示的最后一段并不反映部分进展的数学价值。当然，任何 $O(n^{4/3-\varepsilon})$ 的界都将是对 Spencer–Szemerédi–Trotter [SST84] 自 1984 年以来仅有常数因子改进的估计的一个重大进展 [ÁP22]。

下面我们还逐字复现了内部模型输出的原始解，在任何自动评分或重写之前。

### 内部模型的最终响应

我将使用 Golod-Shafarevich 论证的标准形式，并带有指定的分裂。记 $\operatorname{rd}(L) = |D_L|^{1/[L:\mathbb{Q}]}$。对于一个有限生成的 pro-$p$ 群 $G$，令 $d(G)$ 和 $r(G)$ 分别表示生成元和关系的最小数目，并令 $\Phi(G)$ 为其 Frattini 子群。我将使用以下两个标准事实。首先，如果 $g_1,\dots,g_k \in \Phi(G)$，则 $G$ 除以由 $g_i$ 生成的闭正规子群所得的商群具有相同的生成元秩，且关系秩至多为 $r(G) + k$。其次，一个具有 $d$ 个生成元和 $r$ 个关系的有限 pro-$p$ 群满足 $r > d^2/4$。我在塔构造中使用 $p = 3$（这避免了所有二进无限素数问题）。

令 $\ell$ 很大。选择不同的素数 $r_1,\dots,r_\ell \equiv 1 \pmod{3}$，取前 $\ell$ 个这样的素数，并令 $L_i$ 为 $\mathbb{Q}(\zeta_{r_i})$ 的三次循环子域。令 $D = \prod_i r_i$ 且 $M = L_1 \cdots L_\ell$。因此 $\operatorname{Gal}(M/\mathbb{Q}) \cong (\mathbb{Z}/3\mathbb{Z})^\ell$。如果 $\chi_i$ 是导子为 $r_i$ 的三次特征，令 $F$ 为对应于特征 $\chi_1 \cdots \chi_\ell$ 的三次循环子域。由导子-判别式公式，$|D_F| = D^2$。实际上，$F$ 的两个非平凡特征都具有导子 $D$。类似地，$M$ 的每个特征形如 $\prod_i \chi_i^{a_i}$，$a_i \in \{0,1,2\}$，其导子为那些 $a_i \neq 0$ 的 $r_i$ 的乘积。因此每个 $r_i$ 出现在 $2 \cdot 3^{\ell-1}$ 个非平凡特征中，所以
$$|D_M| = D^{2 \cdot 3^{\ell-1}} = |D_F|^{[M:F]}.$$
因此 $M/F$ 处处无分歧。所有这些域都是完全实的。因此，如果 $G$ 是 $F$ 的最大无分歧 pro-3 扩张的 Galois 群，则
$$d(G) \ge \ell - 1. \tag{1}$$
（我们有初等阿贝尔无分歧扩张 $M/F$。）由于 $F$ 是完全实三次域且不包含 $\zeta_3$，Shafarevich 对无分歧 pro-3 群的关系秩估计给出
$$r(G) \le d(G) + C_0 \tag{2}$$
其中 $C_0$ 是一个绝对常数（任何具有绝对常数的线性界在这里都足够）。此外，
$$\log \operatorname{rd}(F) = \frac{2}{3} \log D = O(\ell \log \ell). \tag{3}$$
令 $E/F$ 为对应于 $G/\Phi(G)$ 的有限初等阿贝尔扩张。令 $d = d(G)$ 且
$$t = \left\lfloor \frac{d^2}{100} \right\rfloor.$$
由 Chebotarev，选择不同的有理素数 $q_1,\dots,q_t$，避开 $3D$，它们在 $E(i)$ 在 $\mathbb{Q}$ 上的正规闭包中完全分裂。则每个 $q_b \equiv 1 \pmod{4}$，每个 $q_b$ 在 $F$ 中完全分裂，并且对于 $F$ 在 $q_b$ 上的每个素除子 $v$，Frobenius 元素在 $G$ 中位于 $\Phi(G)$ 内。有 $3t$ 个这样的素除子 $v$。用这些 Frobenius 元素生成的闭正规子群除 $G$。由上述群论观察，商群具有生成元秩 $d$ 和至多 $r(G) + 3t$ 个关系；对于大的 $\ell$，(2) 给出 $r(G) + 3t < d^2/4$。因此这个商群是无限的。在其中，所有 $q_b$ 之上的素除子的分解群是平凡的（扩张是无分歧的），所以 $q_b$ 完全分裂。取一个递降的开正规子群链给出一个无限塔
$$F = F_0 \subset F_1 \subset F_2 \subset \cdots$$
的有限无分歧扩张，其中每个 $q_b$ 完全分裂。由于扩张具有 3-幂次 Galois 群，塔中的所有域都是完全实的。记 $f_j = [F_j : \mathbb{Q}]$；则 $f_j \to \infty$ 且 $\operatorname{rd}(F_j) = \operatorname{rd}(F)$。现在令 $K_j = F_j(i)$，具有复共轭 $c$。添加 $i$ 的相对判别式整除 $(4)$，所以
$$\operatorname{rd}(K_j) \le 2 \operatorname{rd}(F) =: A_\ell. \tag{4}$$
我们将使用基本界：如果 $[L:\mathbb{Q}] = n$ 且 $\operatorname{rd}(L) \le A$，则
$$h(L) \le C(A)^n, \quad \log C(A) = O(\log A + \log\log(3A)). \tag{5}$$
实际上，Minkowski 在每个理想类中给出一个范数 $X \le (C\sqrt{A})^n$ 的整理想。范数为 $m$ 的理想数目至多为 $n$ 重除数函数 $d_n(m)$，且
$$\sum_{m \le X} d_n(m) \le C^n X (1 + \log X)^{n-1} / (n-1)!,$$
当 $\log X = O_A(n)$ 时在 $n$ 上呈指数增长。由 (4),(5) 我们得到
$$h(K_j) \le H_\ell^{f_j}, \quad \log H_\ell = O(\ell \log \ell). \tag{6}$$
令 $Q = \prod_{b=1}^t q_b$。对于固定的 $j$，每个 $q_b$ 在 $F_j$ 中有 $f_j$ 个一次素除子，且这些素除子中的每一个在 $K_j$ 中分裂为一对共轭素除子 $P_s, cP_s$。因此有 $m = t f_j$ 个这样的对。对于 $\varepsilon = (\varepsilon_s) \in \{0,1\}^m$，令
$$A_\varepsilon = \prod_{\varepsilon_s = 1} P_s \prod_{\varepsilon_s = 0} cP_s.$$
这些理想中至少有 $2^m / h(K_j)$ 个位于同一个理想类中。固定这样一个纤维中的一个元素 $\eta$。对于纤维中的每个 $\varepsilon$，选择 $\alpha_\varepsilon \in K_j^*$ 满足 $(\alpha_\varepsilon) = A_\varepsilon A_\eta^{-1}$，并定义
$$u_\varepsilon = \alpha_\varepsilon / c(\alpha_\varepsilon).$$
对于 $K_j$ 的每个复嵌入 $\sigma$，$\sigma(c\alpha) = \overline{\sigma(\alpha)}$，因此 $|\sigma(u_\varepsilon)| = 1$。$u_\varepsilon$ 的有限赋值支撑在 $\mathbb{Q}$ 之上且取值在 $\{-2,0,2\}$ 中，所以 $Q^2 u_\varepsilon \in \mathcal{O}_{K_j}$。在素除子 $P_s$ 处，赋值为 $2(\varepsilon_s - \eta_s)$，因此 $u_\varepsilon$ 互不相同。由 (6)，对于大的 $\ell$，
$$|U_j| \ge \frac{2^{t f_j}}{h(K_j)} \ge \exp(\gamma f_j), \quad \gamma := t \log 2 - \log H_\ell > 0, \tag{7}$$
其中 $U_j$ 表示这组元素。通过从每个共轭对中选择一个嵌入，将 $K_j$ 嵌入 $V_j = \mathbb{C}^{f_j}$，并令 $\Lambda_j = Q^{-2} \mathcal{O}_{K_j}$ 在此 Minkowski 嵌入中。则 $U_j \subset \Lambda_j$，且每个 $u \in U_j$ 的每个坐标的模为 $1$。固定 $R > 1/2$。令 $W \subset V_j$ 为圆盘 $|z| \le R$ 的乘积。记 $b = \pi R^2$，并令 $a = a(R)$ 为两个半径为 $R$、圆心距离为 $1$ 的圆盘的重叠面积；令 $\rho_R = a/b$，所以 $\rho_R \to 1$ 当 $R \to \infty$。对于陪集 $y + \Lambda_j$，令 $X_y = (y + \Lambda_j) \cap W$，并令 $D_y$ 为满足 $x, x+u \in X_y$ 且 $u \in U_j$ 的有序对 $(x, x+u)$ 的数目。在环面 $V_j / \Lambda_j$ 上平均给出
$$\mathbb{E}|X_y| = \frac{b^{f_j}}{\operatorname{covol}(\Lambda_j)}, \quad \mathbb{E} D_y = \frac{|U_j| a^{f_j}}{\operatorname{covol}(\Lambda_j)}.$$
因此某个陪集满足 $D_y \ge |U_j| \rho_R^{f_j} |X_y|$。选择 $R$ 足够大使得 $\log \rho_R > -\gamma/2$。对于这个陪集，记 $X = X_y$，(7) 给出
$$D_y \ge e^{\gamma f_j / 2} |X|. \tag{8}$$
将 $X$ 投影到第一个复坐标。这个投影在 $\Lambda_j$ 的陪集上是单射：如果两个点具有相同的第一个坐标，它们的差是 $K_j$ 中一个共轭为零的元素，因此为零。令 $P_j \subset \mathbb{C} \cong \mathbb{R}^2$ 为投影集，$n_j = |P_j| = |X|$。(8) 中计数的每个有序对投影为单位线段，因为 $u$ 的第一个坐标的模为 $1$。对于固定的有序端点，差（从而 $u$）是唯一的，因此一个无序线段最多被计数两次。因此
$$\nu(P_j) \ge \frac{1}{2} e^{\gamma f_j / 2} n_j. \tag{9}$$
最后，如果 $0 \neq \lambda \in \Lambda_j$，则 $\beta = Q^2 \lambda$ 是一个非零代数整数，且对于所选的嵌入，
$$\prod_{r=1}^{f_j} |\sigma_r(\lambda)| = |N_{K_j/\mathbb{Q}}(\beta)|^{1/2} Q^{-2f_j} \ge Q^{-2f_j}.$$
因此 $\lambda$ 的某个坐标的模至少为 $Q^{-2}$。在多圆盘 $W$ 中的一个堆积论证给出
$$n_j \le (C R Q^2)^{2f_j} = e^{B f_j} \tag{10}$$
其中 $B$ 与 $j$ 无关。此外，(8) 和 $D_y \le n_j^2$ 蕴含 $n_j \ge e^{\gamma f_j / 2}$，所以 $n_j \to \infty$。结合 (9) 和 (10)，并吸收因子 $1/2$（对大的 $j$），我们得到
$$\nu(P_j) \ge n_j^{1+\delta}, \quad \delta = \frac{\gamma}{4B} > 0. \tag{11}$$
给定任意 $C_0 > 0$ 和 $N$，选择 $j$ 足够大使得 $n_j \ge N$ 且 $C_0 / \log\log n_j < \delta$。则
$$\nu(n_j) \ge \nu(P_j) > n_j^{1 + C_0 / \log\log n_j}.$$
因此不存在通用常数 $C,N$ 能满足所提议的上界。

本文的其余部分更详细地解释了上述证明。

---

## 2 从数域构造平面点集

假设存在下面定义的可允许域，我们构造具有许多单位距离的平面点集。第 3 节提供这些域。

**定义 2.1.** 一个**可允许数据**由以下组成：
- 一个完全实数域 $L$，次数 $f = [L:\mathbb{Q}]$；
- CM 域 $K = L(i)$，在 $L$ 上具有非平凡自同构 $c$（见定义 A.4）；
- 一个正整数 $t$，即所选有理素数的个数；
- 不同的有理素数 $q_1,\dots,q_t$，每个满足 $q_b \equiv 1 \pmod{4}$ 且在 $L$ 中完全分裂（关于分裂的定义见定义 A.2）。

令 $Q = \prod_{b=1}^t q_b$。在几何部分中，我们也记 $D = Q^2$ 为相应的固定分母。

每个 $q_b$ 在 $K = L(i)$ 中给出许多共轭素理想对。由于 $q_b$ 在 $L$ 中完全分裂，它在 $L$ 中给出 $f$ 个素理想 $\mathfrak{q}$，每个具有剩余域 $\mathcal{O}_L/\mathfrak{q} \cong \mathbb{F}_{q_b}$。由于 $q_b \equiv 1 \pmod{4}$，多项式 $x^2 + 1$ 在这个剩余域上分裂，所以每个 $\mathfrak{q}$ 在 $K$ 中分裂。因此固定的有理素数给出 $m = t f$ 个 $K$ 的共轭素理想对：
$$\{P_s, cP_s\}, \quad s = 1,\dots,m. \tag{2}$$

**命题 2.2.** 令 $L, K, t, q_1,\dots,q_t, Q$ 为定义 2.1 意义上的可允许数据。假设对某个实数 $H > 0$ 有 $h(K) \le H^f$。则存在一个集合 $U \subset Q^{-2} \mathcal{O}_K$，使得每个 $u \in U$ 满足 $N_{K/L}(u) = 1$，其中对于 $K = L(i)$，相对范数为 $N_{K/L}(u) = u c(u)$。每个 $u \in U$ 还对每个复嵌入 $\sigma: K \hookrightarrow \mathbb{C}$ 满足 $|\sigma(u)| = 1$。此外，
$$|U| \ge \exp\{(t \log 2 - \log H) f\}.$$

**证明。** 对每个二元向量 $\varepsilon = (\varepsilon_s) \in \{0,1\}^m$，从 (2) 中的每个共轭对中选择一个素数并令
$$A_\varepsilon = \prod_{\varepsilon_s = 1} P_s \prod_{\varepsilon_s = 0} cP_s.$$
这 $2^m$ 个理想不一定是主理想，但它们只占据 $h(K)$ 个理想类。因此映射 $\varepsilon \mapsto [A_\varepsilon] \in \operatorname{Cl}(K)$ 的某个纤维的大小至少为 $2^m / h(K)$。固定这样一个纤维中的一个向量 $\eta$；对于同一纤维中的每个 $\varepsilon$，$A_\varepsilon A_\eta^{-1}$ 是主理想，所以选择 $\alpha_\varepsilon \in K^\times$ 满足 $(\alpha_\varepsilon) = A_\varepsilon A_\eta^{-1}$，并令
$$u_\varepsilon = \alpha_\varepsilon / c(\alpha_\varepsilon).$$
则 $u_\varepsilon c(u_\varepsilon) = 1$，所以 $N_{K/L}(u_\varepsilon) = 1$。由于 $L$ 是完全实的，$c$ 在 $K$ 的每个复嵌入下变为普通的复共轭。因此
$$|\sigma(u_\varepsilon)| = \left|\frac{\sigma(\alpha_\varepsilon)}{\overline{\sigma(\alpha_\varepsilon)}}\right| = 1. \tag{3}$$
令 $U$ 为从此纤维获得的所有 $u_\varepsilon$ 的集合。$u_\varepsilon$ 的主理想为
$$(u_\varepsilon) = A_\varepsilon A_\eta^{-1} c(A_\varepsilon A_\eta^{-1}).$$
因此，在所选的素数处，
$$v_{P_s}(u_\varepsilon) = 2(\varepsilon_s - \eta_s), \quad v_{cP_s}(u_\varepsilon) = -2(\varepsilon_s - \eta_s). \tag{4}$$
显示的理想恒等式和 (4) 表明 $u_\varepsilon$ 的所有极点阶数至多为 $2$ 且位于 $q_b$ 之上。由于 $Q \mathcal{O}_K$ 在每个这样的素数处赋值为 $1$，$Q^2 u_\varepsilon \in \mathcal{O}_K$。所以 $u_\varepsilon \in Q^{-2} \mathcal{O}_K$。

由 (4)，不同的 $\varepsilon$ 给出不同的赋值向量，因此给出不同的元素 $u_\varepsilon$。因此
$$|U| \ge \frac{2^{t f}}{h(K)} \ge \exp\{(t \log 2 - \log H) f\}.$$

令 $\gamma := t \log 2 - \log H$。以下结果是证明的几何部分：一列具有相同分裂有理素数和 $\gamma > 0$ 的可允许域已经给出了所需的平面点集。

**定理 2.3.** 假设存在一列可允许数据 $(L_j, K_j = L_j(i), q_1,\dots,q_t)$，具有相同的有理素数 $q_1,\dots,q_t$，次数 $f_j = [L_j:\mathbb{Q}] \to \infty$，以及一个与 $j$ 无关的常数 $H > 0$，使得 $h(K_j) \le H^{f_j}$ 且 $\gamma := t \log 2 - \log H > 0$。则存在常数 $\delta > 0$ 和无穷多个 $n$ 使得 $\nu(n) \ge n^{1+\delta}$。

为了证明定理 2.3，固定序列中的一个可允许数据并省略下标 $j$。因此 $f = [L:\mathbb{Q}]$，$K = L(i)$，素数 $q_b$ 及其乘积 $Q$ 是固定的。命题 2.2 给出 $|U| \ge e^{\gamma f}$，其中 $\gamma = t \log 2 - \log H$。令 $D = Q^2$，使得 $U \subset D^{-1} \mathcal{O}_K$。接下来的两个小节构造相应的有限平面集。

### 2.1 选择窗口并投影

在固定一个可允许数据后，命题 2.2 提供的集合 $U$ 给出了许多范数为一的元素，这些元素将作为 Minkowski 格中的平移。我们选择这个格的一个随机平移，将点保留在圆盘乘积内部，并计数差在 $U$ 中的对。

对于 $L$ 的每个实嵌入，选择一个扩张 $\sigma_r: K \hookrightarrow \mathbb{C}$，$r = 1,\dots,f$，并使用 Minkowski 映射
$$\Phi: K \to V = \mathbb{C}^f, \quad \Phi(x) = (\sigma_1(x),\dots,\sigma_f(x)).$$
我们将分式理想 $D^{-1} \mathcal{O}_K$ 与格 $\Lambda = \Phi(D^{-1} \mathcal{O}_K) \subset V$ 等同，并将 $U$ 的像 $\Phi(U) \subset \Lambda$ 也记作 $U$。

下面的有界性条件是阿基米德条件。对于 $z = (z_1,\dots,z_f) \in V$，令 $\|z\|_\infty = \max_{1 \le r \le f} |z_r|$，并令 $B_R = \{z \in V : \|z\|_\infty \le R\}$。因此 $B_R$ 是 $f$ 个半径为 $R$ 的圆盘的乘积。

对于陪集 $a + \Lambda$，定义 $X_a = (a + \Lambda) \cap B_R$，$N_a = |X_a|$，以及
$$E_a = \#\{(x,x') \in X_a^2 : x' - x \in U\}.$$
因此 $N_a$ 计数格陪集中有界范数的格点，而 $E_a$ 计数其中差为我们范数为一的平移之一的有序对。

令 $b(R) = \pi R^2$ 为一个半径为 $R$ 的圆盘的面积，令 $a(R)$ 为两个半径为 $R$、圆心距离为 $1$ 的圆盘的重叠面积——由 (3)，$U$ 中每个平移的坐标大小——并令 $\rho_R = a(R)/b(R)$。则 $\rho_R \to 1$ 当 $R \to \infty$。

**引理 2.4.** 选择 $R > 1/2$ 足够大使得 $\log \rho_R > -\gamma/2$。则某个非空陪集 $a + \Lambda$ 满足
$$E_a \ge e^{\gamma f / 2} N_a.$$

**证明。** 在 $a \in V/\Lambda$ 上关于 Haar 概率测度平均，标准的展开恒等式给出
$$\mathbb{E}_a[N_a] = \frac{\operatorname{vol}(B_R)}{\operatorname{covol}(\Lambda)} = \frac{b(R)^f}{\operatorname{covol}(\Lambda)}.$$
对于固定的 $u \in U$，满足 $x' - x = u$ 的对对应于 $(a + \Lambda) \cap B_R \cap (B_R - u)$ 中的点。由 (3)，这个 Minkowski 空间平移的每个坐标的绝对值均为 $1$。因此 $\operatorname{vol}(B_R \cap (B_R - u)) = a(R)^f$。对 $u \in U$ 求和并在环面上平均给出
$$\mathbb{E}_a[E_a] = \frac{|U| a(R)^f}{\operatorname{covol}(\Lambda)} = |U| \rho_R^f \mathbb{E}_a[N_a].$$
如果每个非空陪集都有 $E_a < |U| \rho_R^f N_a$，那么对所有陪集积分会与上述恒等式矛盾；空陪集对两边贡献为零。因此某个非空陪集有 $E_a \ge |U| \rho_R^f N_a$。使用 $|U| \ge e^{\gamma f}$ 和 $R$ 的选择给出 $E_a \ge e^{\gamma f/2} N_a$。

固定引理 2.4 提供的一个陪集，并记 $X = X_a$ 和 $N = |X|$。现在可以使用所选的复坐标之一来获得平面集。为具体起见，令 $\pi_1: V \to \mathbb{C}$ 为第一个坐标投影，对应于嵌入 $\sigma_1$，并令 $P = \pi_1(X) \subset \mathbb{C} \cong \mathbb{R}^2$。

**引理 2.5.** 映射 $\pi_1: X \to \mathbb{C}$ 是单射。此外，
$$\nu(P) \ge \frac{1}{2} e^{\gamma f/2} |P|.$$

**证明。** 如果 $x, x' \in X$ 且 $\pi_1(x) = \pi_1(x')$，则 $x - x' = \Phi(D^{-1} \beta)$ 对某个 $\beta \in \mathcal{O}_K$，且 $\sigma_1(\beta) = 0$。由于 $\sigma_1$ 是域嵌入，$\beta = 0$，所以 $x = x'$。因此 $|P| = |X| = N$。

$E_a$ 计数的每个有序对形如 $(x, x+u)$，其中 $u \in U$，它投影为一个有序单位距离对，因为 $|\pi_1(x+u) - \pi_1(x)| = |\pi_1(u)| = 1$。$\pi_1$ 在 $X$ 上的单射性表明 $X^2$ 中不同的有序对给出不同的有序平面对。由于每个无序单位线段最多有两个方向，
$$2\nu(P) \ge E_a \ge e^{\gamma f/2} |P|.$$

### 2.2 大小界

引理 2.5 给出了相对于域次数的许多单位距离。为了将其转化为关于 $n = |P|$ 的陈述，我们需要一个在有限窗口中能容纳的点数的统一指数上界。这是在阿基米德上确界范数中的一个堆积估计。

**引理 2.6.** 令 $n = |P|$。则 $n \le e^{B f}$，其中 $B = 2 \log(4 R D)$。

**证明。** 由于 $\pi_1$ 在 $X$ 上是单射，只需界住 $|X|$。如果 $x \neq x'$ 在