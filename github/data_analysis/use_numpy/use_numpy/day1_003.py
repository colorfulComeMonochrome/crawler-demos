import numpy as np



# 1、创建一个长度为10的一维全为0的ndarray对象
# 然后让第5个元素等于1
"""
arr1 = np.zeros(10)
arr1[4] = 1
print(arr1)
"""

# 2、创建一个元素为从 10 到 49 的 ndarray 对象
"""
arr2 = np.arange(10, 50, 1)
print(arr2)
"""
# 3、将第2题的所有元素位置反转
# arr2 = np.arange(49, 9, -1)
# arr2 = np.arange(10, 50, 1)
# arr2 = arr2[::-1]
# print(arr2)
# 4、使用np.random.random创建一个10*10的ndarray对象
# 并打印出最大最小元素
# arr3 = np.random.random(100).reshape(10, 10)
# arr3 = np.random.randint(0, 100, size=[10, 10])
# print(arr3)
# print(arr3.max())
# print(arr3.min())
# print(type(arr3.min()))
# 5、创建一个10*10的ndarray对象，且矩阵边界全为1，里面全为0
# arr5 = np.ones((10, 10))
# print(arr5)
# arr5[1:-1, 1:-1] = 0
# print(arr5)
# arr5_1 = np.zeros((10, 10))
# arr5_1[[0,-1], :] = 1
# arr5_1[:,[0,-1]] = 1
# print(arr5_1)

# 6、创建一个每一行都是从0到4的5*5矩阵
# arr6 = np.zeros((5, 5))
# arr6_1 = arr6 + [0, 1, 2, 3, 4]
# print(arr6_1)

# 7、创建一个范围在(0,1)之间的长度为12的等差数列
# arr7 = np.linspace(0, 1, 12)
# print(arr7)
# 8、创建一个长度为10的随机数组并排序
# arr8 = np.random.randint(0, 100, 10)
# print(arr8)
# arr8.sort()
# print(arr8)
# 9、创建一个长度为10的随机数组并将最大值替换为0
# arr9 = np.random.randint(0, 100, 10)
# print(arr9)
# index = arr9.argmax()
# arr9[index] = 0
# print(arr9)
# 10、如何根据第3列来对一个 5*5 矩阵排序？
# arr10 = np.random.randint(0, 100, size=(5, 5))
# print(arr10)
# index = arr10[:, 2].argsort()
# print(index)
# print(arr10[index])
# 12、给定数组[1, 2, 3, 4, 5]
# 如何得到在这个数组的每个元素之间插入3个0后的新数组？
# arr12 = np.array([1, 2, 3, 4, 5])
# arr12_1 = np.zeros(len(arr12) * 4 - 3)
# print(arr12)
# print(arr12_1)
# arr12_1[0::4] = arr12
# print(arr12_1)
# 13、给定一个二维矩阵，如何交换其中两行的元素？
# arr13 = np.random.randint(0, 100, size=[4, 3])
# print(arr13)
# arr13[[0, 1], :] = arr13[[1, 0], :]
# print(arr13)
# 14、生成一个二维数组，并实现行或列反转
# arr14 = np.random.randint(0, 100, size=[4, 3])
# print(arr14)
# # 行列一起转  (中心对称)
# arr14_1 = arr14[::-1, ::-1]
# print(arr14_1)

# 15、创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积


# 16、矩阵的每一行的元素都减去该行的平均值
# arr16 = np.random.randint(0, 30, size=[5, 4])
# print(arr16)
# avg = arr16.mean(axis=1).reshape(5, 1)
# print(avg)
# print(arr16 - avg)

'''
# 17、打印出以下函数（要求使用np.zeros创建8*8的矩阵）：
[[0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]]
'''
# arr17 = np.zeros((8, 8))
# arr17[1::2, 0::2] = 1
# arr17[0::2, 1::2] = 1
# print(arr17)
# 18、正则化一个5*5随机矩阵
# 正则的概念：假设a是矩阵中的一个元素，
# max/min分别是矩阵元素的最大最小值，
# 则正则化后a = (a - min)/(max - min)

# arr18 = np.random.randint(0, 100, size=(5, 5))
# print(arr18)
# arr_max = arr18.max()
# arr_min = arr18.min()
# arr = (arr18 - arr_min) / (arr_max - arr_min)
# print(arr)
'''
19、将一个一维数组转化为二进制表示矩阵。例如
[1,2,3]
转化为
[[0,0,1],
[0,1,0],
[0,1,1]]
'''
arr19 = np.random.randint(0, 10, 4)
print(arr19)



































