import numpy as np


def pivot(d, B, bn):
    in_num = np.argmax(d[-1][:-1])  # 入基下标 # numpy.argmax(array, axis)用于返回一个numpy数组中最大值的索引值
    print("入基下标："+ str(in_num))

    print("θi")
    all_sita = d[:-1, -1] / np.maximum(0, d[:-1, in_num])  # 求θi ，np.maximum(A, B) 最少接收兩個參數，回傳A與B逐個比較的最大值
    print(all_sita)
    np.place(all_sita, np.isnan(all_sita), np.inf)  # np.nan替换为np.inf
    out_num = np.argmin(all_sita)  # 出基下标 # numpy.argmin(array, axis) 用于返回一个numpy数组中最小值的索引值
    print("出基下标："+ str(out_num))

    B[out_num] = in_num  # 更新基变量,这一步很绕

    print("换基后，所有基的下标")
    print(B)

    d[out_num] /= d[out_num][in_num]  # 将新入基的系数化为1
    for i in range(bn):
        if i != out_num :
            d[i] -= d[i][in_num] * d[out_num]
    print(d)
    return d, B


def solve(d, B, bn):
    flag = True
    i = 1
    while flag:
        if max(d[-1][:-1]) <= 0:  # 直至所有系数小于等于0
            flag = False
        else:
            print("======================")
            print("第"+ str(i) +"次pivot：")
            d, B = pivot(d, B, bn)
            i+=1
    return d, B


def print_sol(d, B):
    print("======================")
    for i in range(d.shape[1] - 1):
        print("x%d=%.2f" % (i, d[B.index(i)][-1] if i in B else 0))
    print("objective is %.2f" % (-d[-1][-1]))


dstr = '''2 1 1 0 40
1 3 0 1 30
3 4 0 0 0'''
d = np.array([[eval(dij) for dij in dj.split(' ')] for dj in dstr.splitlines()]).astype(np.float)
(bn, cn) = d.shape  # bn矩阵的行数，cn矩阵的列数
B = list(range(cn - bn, cn - 1))  # 初始基变量的下表组成的列表
print("初始化：")
print(B)
print(d)
d, B = solve(d, B, bn)
print_sol(d, B)