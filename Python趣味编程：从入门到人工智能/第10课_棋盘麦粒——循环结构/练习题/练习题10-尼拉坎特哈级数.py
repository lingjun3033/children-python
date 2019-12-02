'''
程序：用尼拉坎特哈级数计算圆周率近似值
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
pi, n, op = 3, 2, -1
i = 0
while i < 15000:
    op = -1 * op
    pi = pi + op * 4 / (n * (n+1) * (n+2))
    n += 2
    i += 1
print(pi)
