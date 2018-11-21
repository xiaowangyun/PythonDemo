#
# coding:utf-8
# 输入输出

# 读取键盘输入
# read = input("请输入一句话\n")
# print(read)

s = 'Hello World'
print(str(s))
print(repr(s))

s = 'Hello \n World'
print(str(s))
print(repr(s))

for i in range(1, 4):
    print(repr(i).rjust(1), repr(i * i).rjust(2), end=' ')
    print(repr(i * i * i).rjust(3))

for i in range(1, 4):
    print('{0:d}{1:3d}{2:4d}'.format(i, i * i, i * i * i))

print('{} like {}'.format('I', 'Python'))

print('欢迎{0}来到{1}，网址：{site}'.format('孙小北', '小望云', site='www.xiaowangyun.com'))

import math

print("PI近似值为：{0:.3f}".format(math.pi))

site = {'百度': 'www.baidu.com', '小望云': 'www.xiaowangyun.com'}
for name, url in site.items():
    print('{0:5}-->{1:10}'.format(name, url))


## 循环输入
# while True:
#     num = int(input("请输入一个数字 :"))
#     print("你输入的数字是：", num)
