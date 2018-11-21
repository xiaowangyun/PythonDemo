# coding:utf-8
'''
斐波那契(fibonacci)数列模块
'''


# 求n以内的斐波那契数列
def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


# 求第m个斐波那契数 第n项（从0开始，第0项为0）
def fib2(m):
    result = [0, 1]
    a, b = 0, 1
    if m <= 0:
        return 0
    for i in range(2, m + 1):
        result.append(result[i-1]+result[i-2])
    return result[m]
