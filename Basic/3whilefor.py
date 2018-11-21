#
# coding utf-8
count = 5
while count > 0:
    print(count)
    count = count - 1

#  1<=i<5
for i in range(1, 5):
    print(i)

# 遍历序列，列表或字符串
for letter in "Python":
    print(letter)
print("Python")

# 直接遍历元素
letterList = ['A', 'B', 'C', 'D', 'E']
for letter in letterList:
    print(letter)

# 序列索引迭代
for i in range(len(letterList)):
    print(letterList[i])

# For循环使用else语句
# 求a，b数之间的质数
a = 5
b = 10
for num in range(a, b):
    for i in range(2, num):
        if num % i == 0:
            print(num, '=', i, '*', num // i)
            break
    else:
        print(num, '是质数')

# For循环使用else语句
# 求a，b数之间的质数   else 位置写错
a = 5
b = 10
for num in range(a, b):
    for i in range(2, num):
        if num % i == 0:
            print(num, '=', i, '*', num // i)
            break
        else:
            print(num, '是质数')

# break 和 continue 语句
for i in range(1, 5):
    if (i == 2):
        break
    print(i)
for i in range(1, 5):
    if (i == 2):
        continue
    print(i)

for letter in "Python":
    if (letter == 'o'):
        pass
        print('执行pass块')
    print(letter)

# if elif else 语句

num = int(input())
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不能整除 2 和 3")


