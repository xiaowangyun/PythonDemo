
# coding: utf-8

import time

# 矩阵库
# import numpy as np

print(time.asctime())

a = [2, 3, 5]
a.append(4)
a.insert(1, 3)
a.pop(2)
a.sort()


def add(a, b):
    c = a + b
    return c


print(a)
# demo
print(add(3, 5))

print(bin(100))

print(bin(100)[2:])
