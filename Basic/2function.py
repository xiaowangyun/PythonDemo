# coding:utf-8

'''
Python 函数
'''


# 函数定义
def hello():
    print("Hello World")


# 函数调用
hello()


# 两数之和
def add(a, b):
    print('a+b=', a + b)


# 函数调用
add(3, 4)


# 可更改(mutable)与不可更改(immutable)对象
def mutable_demo(a, list):
    a = 5
    list[2] = 0
    list.append(5)


d = 1
e = [1, 2, 3, 4]
# mutable_demo(d, e)
mutable_demo(a=d, list=e)
print(d)
print(e)


def print_info(name, age=18, sex='女'):
    "打印人员信息"
    print("名字: ", name, " 年龄: ", age, "性别: ", sex)


# 调用
print_info("小望云")
print_info("小望云", age=21)
print_info("小望云", age=25, sex='男')


# 不定长参数
def print_info2(name, *group):
    print("名字: ", name)
    print(group)
    for var in group:
        print(var)


# 调用
print_info2("小望云")
print_info2("小望云", 18)
print_info2("小望云", 18, '男')


# 不定长参数
def print_info3(name, **group):
    print("名字: ", name)
    print(group)


# 调用
print_info3("小望云")
print_info3("小望云", age=18)
print_info3("小望云", age=18, sex='男')


# 函数返回值
def add_demo2(a, b):
    return a + b


# 调用
sum = add_demo2(4, 5)
print(sum)

b_num = 100  # 内建变量

g_num = 0  # 全局变量


def outer_fun():
    o_num = 1  # 闭包函数外的函数

    def inner():
        i_num = 2  # 局部变量


c = 5  # 全局变量
d = 6  # 全局变量


# 函数返回值
def add_demo3(a, b):
    temp = a + b  # 局部变量
    return temp


# 调用
sum = add_demo3(c, d)  # 全局变量
print(sum)

num = 1  # 全局变量


def global_fun():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


global_fun()
print(num)

temp = 1


def outer():
    temp = 10

    def inner():
        nonlocal temp  # nonlocal关键字声明
        temp = 100
        print(temp)

    inner()
    print(temp)


outer()
print(temp)

a = 10


def test(a):
    a = a + 1
    print(a)


test(a)
