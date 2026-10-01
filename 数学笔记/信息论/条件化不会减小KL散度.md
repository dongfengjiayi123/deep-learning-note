---

title: 条件化不会减小KL散度  
aliases:

- Conditioning never decreases divergence
    
- 条件散度不小于边缘散度  
    tags:
    
- 信息论
    
- KL散度
    
- Jensen不等式
    
- 对数和不等式
    

---

# 条件化不会减小 KL 散度

## 结论

设离散随机变量 (X,\hat X) 具有相同字母表，(Z) 为条件变量，则

[  
\boxed{  
D!\left(P_{X|Z}\middle|P_{\hat X|Z}\mid P_Z\right)  
\ge  
D(P_X|P_{\hat X})  
}  
]

其中

# [  
D!\left(P_{X|Z}\middle|P_{\hat X|Z}\mid P_Z\right)

\sum_z P_Z(z)  
D!\left(P_{X|Z=z}\middle|P_{\hat X|Z=z}\right).  
]

即：**知道条件 (Z) 后所观察到的平均分布差异，不小于忽略 (Z) 后的分布差异。**

---

## 证明思路

记

[  
p_z=P_Z(z),\qquad  
p_{x|z}=P_{X|Z}(x|z),\qquad  
q_{x|z}=P_{\hat X|Z}(x|z).  
]

条件散度可以写为

# [  
D!\left(P_{X|Z}\middle|P_{\hat X|Z}\mid P_Z\right)

\sum_x\sum_z  
p_zp_{x|z}  
\log\frac{p_zp_{x|z}}{p_zq_{x|z}}.  
]

对固定的 (x)，令

[  
a_z=p_zp_{x|z},\qquad  
b_z=p_zq_{x|z}.  
]

由[[对数和不等式]]，

[  
\sum_z a_z\log\frac{a_z}{b_z}  
\ge  
\left(\sum_z a_z\right)  
\log  
\frac{\sum_z a_z}{\sum_z b_z}.  
]

又因为

[  
\sum_z a_z=P_X(x),\qquad  
\sum_z b_z=P_{\hat X}(x),  
]

所以

[  
\sum_z  
p_zp_{x|z}  
\log\frac{p_{x|z}}{q_{x|z}}  
\ge  
P_X(x)\log\frac{P_X(x)}{P_{\hat X}(x)}.  
]

对 (x) 求和，得到

[  
D!\left(P_{X|Z}\middle|P_{\hat X|Z}\mid P_Z\right)  
\ge  
D(P_X|P_{\hat X}).  
]

---

## 与 Jensen 不等式的关系

该结论可以看作由 [[Jensen不等式]] 推出，因为对数和不等式来自凸函数

[  
\varphi(t)=t\log t.  
]

设

[  
A=\sum_z a_z,\qquad  
B=\sum_z b_z,\qquad  
\lambda_z=\frac{b_z}{B},  
]

则 Jensen 不等式给出

[  
\sum_z\lambda_z  
\varphi!\left(\frac{a_z}{b_z}\right)  
\ge  
\varphi!\left(  
\sum_z\lambda_z\frac{a_z}{b_z}  
\right),  
]

从而得到

[  
\sum_z a_z\log\frac{a_z}{b_z}  
\ge  
A\log\frac AB.  
]

因此，更准确地说：

> 本引理由 Jensen 不等式导出的对数和不等式证明，也可视为 [[KL散度]] 联合凸性的直接结果。

---

## 直观理解

忽略 (Z) 相当于将不同 (Z=z) 下的条件分布混合：

[  
P_X=\sum_z P_Z(z)P_{X|Z=z}.  
]

分布混合会掩盖部分差异，因此

[  
\text{混合后的散度}  
\le  
\text{各条件散度的加权平均}.  
]

换言之，**条件信息使我们能够更细致地区分两个分布；丢弃条件信息不会增强这种区分能力。**

---

## 等号条件

对每个固定的 (x)，若

[  
\frac{P_{X|Z}(x|z)}  
{P_{\hat X|Z}(x|z)}  
]

在所有相关的 (z) 上保持不变，则对数和不等式取等号，从而原不等式取等号。

---

## 相关概念

- [[KL散度]]
    
- [[条件KL散度]]
    
- [[Jensen不等式]]
    
- [[对数和不等式]]
    
- [[KL散度的联合凸性]]
    
- [[数据处理不等式]]