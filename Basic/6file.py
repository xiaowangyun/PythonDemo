# coding:utf-8

# 打开文件
file = open('test.txt', 'w')
# 写入内容
num= file.write("欢迎来到小望云北屋 \n唯一网址：www.xiaowangyun.com")
# 关闭文档
file.close()
print(num)

# read()
file = open('test.txt', 'r')
str = file.read()
print(str)
file.close()

# readlines
file = open('test.txt', 'r')
str = file.readlines()
print(str)
file.close()