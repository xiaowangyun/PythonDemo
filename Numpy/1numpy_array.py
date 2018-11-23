# coding:utf-8
# numpy学习和使用

# 1 安装numpy
# conda install numpy

# 导入numpy模块
import numpy as np

# numpy 创建数组
# array：创建数组
# 一维数组
array1 = np.array([1, 2, 3])
print(array1)
# 二维数组(矩阵)
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array2)

# numpy的属性
# ndim:维度
print('number of dim:', array2.ndim)
# shape:行数和列数
print('shape :', array2.shape)
# size:元素个数
print('size:', array2.size)

# dtype：指定数据类型
array2 = np.array([1, 2, 3], dtype=np.int64)
print('dtype:', array2.dtype)

# zeros：创建数据全为0
# m行n列 全0矩阵
array3 = np.zeros((2, 3))
print(array3)

# ones：创建数据全为1
# m行n列 全1矩阵
array4 = np.ones((2, 3))
print(array4)

# empty：创建数据接近0
array5 = np.empty((2, 3))
print(array5)

# arange：按指定范围创建数据,reshape改变数据的形状(行和列）
array6 = np.arange(12).reshape(3, 4)
print(array6)

# 用 arange 创建连续数组 [10 12 14 16 18]
array7 = np.arange(10, 20, 2)  # 步长为2
print(array7)

# linspace：创建线段,等差数列 # 开始端10，结束端20，且分割成5个数据，生成线段
array8 = np.linspace(10, 20, 6)
print(array8)
