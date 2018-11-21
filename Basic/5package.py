#
# coding:utf-8

import numpy as np

a = np.array([1, 2, 3])
print(a)

from Common import fibo as fb

dir(fb)

result = fb.fib(100)
print(result)

result2 = fb.fib2(7)
print(result2)

from Common.fibo import fib

print(fib(100))

