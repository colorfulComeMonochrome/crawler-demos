import numpy as np
"""
ndarray：n-dimensional array object，即多维数组对象，
是python自带的array对象的扩展，
array对象和list对象的区别是array对象的每一个元素都是数值，
而list保存的是每个元素对象的指针，而作为array对象的扩展，
ndarray在科学计算中就非常适合并且功能强大。
"""

# 列表类型:
# ll = [1, 2, 3, 4]
# print(ll)
# print(type(ll))




# 列表变成numpy的 ndarray类型
# arr = np.array([1, 2, 3, 4])
# arr = np.array([[1, 2], [3, 4]])
# print(arr)
# # print(type(arr))
#
# print('#' * 40)
# 遍历
"""
for i in arr:
    print(i)
    print('-------------')
"""

####################################################
# 生成一个一维的 numpy.array对象


# arr = np.arange(0, 10, 1)
# arr = np.random.randint(0, 100, 10)
# 获取n个0-1之间的随机浮点数
# arr = np.random.rand(10)
# 生成n个正态分布的随机数
# randn中 n是normal的意思
# arr = np.random.randn(10)
# 等差数列    有点坑
# arr = np.linspace(1, 100, 20)
# print(arr)


# 将一维数组对象转成二维数组:3行5列
# arr = np.arange(0, 16).reshape(4, 4)
# arr = np.arange(0, 27).reshape(3, 3, 3)
# print(arr)

# 只要元素个数一致, 可以转换维度
# arr = np.arange(0, 8).reshape(2, 4)
# print(arr)
# print(arr.reshape(2, 2, 2))

# 数组的属性
# 维度
# arr = np.arange(0, 8).reshape(2, 4)
# # arr.shape  返回值是元组
# print(arr.shape)

# 元素个数
# print(arr.shape[0])
# print(arr.shape[1])
# print(arr.shape[0] * arr.shape[1])

# arr.ndim  维度数  秩
# print(arr.ndim)
# 行数
# print(len(arr))


# 数组中元素的数据类型
# arr = np.arange(0, 8)
# arr = np.random.rand(0, 8)
# print(arr.dtype)

# 可以指定生成数组的数据类型
# arr = np.arange(0, 10, 1, dtype='int16')
# print(arr.dtype)

# 数组元素字节大小
# 一个字节是8位

################################################
# 其他生成数组的方式:
# 生成元素全为0的数组
# arr = np.zeros([10, 3])
# arr = np.zeros((10, 3))
# print(arr)

# 生成元素全为1的数组
# arr = np.ones((10, 3))
# print(arr)
# print(arr.dtype)

########################################
# 基本运算
# arr1 = np.random.randint(0, 100, size=[4, 3])
# 等价于
# arr1 = np.random.randint(0, 100).reshape(4, 3)
# print(arr1)
# arr2 = np.random.randint(0, 100, size=[4, 3])
# print(arr2)

# 加减法
# 若两个矩阵相加, 需要维度一致
# 若两个矩阵相加, 需要维度一致
# print(arr1 + arr2)


# 乘法
# 不是矩阵乘法
# print(arr1 * arr2)
# 矩阵乘法
# arr3 = np.random.randint(0, 100, size=[4, 3])
# arr4 = np.random.randint(0, 100, size=[3, 3])
#
# print(arr3.dot(arr4))
# print(arr1.__add__(arr2))


# 函数
# arr1 = np.random.randint(0, 100, size=[4, 3])
# print(arr1)
# # sin()
# print(np.sin(arr1))
#
# print(np.sum(arr1))
#
# print(np.max(arr1))
#
# print(np.min(arr1))
#
# # 平均值 average mean 都是
# print(np.average(arr1))
# print(np.mean(arr1))
#
# # 标准差(方差开方)
# print(np.std(arr1))
#
# # argmax()  获取最大值的下标(索引)
# print(np.argmax(arr1))
#
# # 判断
# # 遍历每一个元素来比较出bool值
# print(arr1 < 30)
# print(type(arr1 < 30)) # <class 'numpy.ndarray'>

# ll = [10, 20, 40]
# print(ll < 30)

# 针对轴的运算, 使用axis参数
# 对轴运算其实就是降维
# arr1 = np.random.randint(0, 100, size=[4, 3])
# print(arr1)

# print(arr1.sum(axis=0))     # 等于0 根据y轴相加
# print(arr1.sum(axis=1))     # 等于1 根据x轴相加


# arr2 = np.random.randint(0, 100, size=[4, 3, 3])
# print(arr2)
# print(arr2.sum(axis=2))       # 等于2  根据z轴相加

# 筛选 切片
# arr1 = np.array([0,1,2,3,4,5,6,7])
# arr2 = np.array([[0,1,2,3,4,5,6,7],
#                  [8,9,10,11,12,13,14,15],
#                  [16,17,18,19,20,21,22,23],
#                  [24,25,26,27,28,29,30,31],
#                  [32,33,34,35,36,37,38,39],
#                  [40,41,42,43,44,45,46,47],
#                  [48,49,50,51,52,53,54,55],
#                  [56,57,58,59,60,61,62,63]])

# print(arr2[1:4])   # 跟列表操作没差
# print(arr2[1:4, 0:3])

# 切片赋值
# arr2[1:4, 0:2] = 0      # 列表无法二维切片
# print(arr2)

#####################################################
# 空数据处理
# arr = np.array([1, 2, 3, None])  # 使用None做运算会报错
# arr = np.array([1, 2, 3, np.nan])  # 使用np.nan代替None
# print(arr)
# print(arr + arr)

########################################################
# 广播，不同维度数组之间的运算
# arr = np.array([1, 2, 3])
# print(arr + 3)       # 遍历数组做加法


# arr6 = np.zeros((5, 5))
# arr6_1 = arr6 + [0, 1, 2, 3, 4]
# print(arr6_1)


#########################################################
# 排序
# 一维数组排序
# arr = np.random.randint(0, 100, 10)
# print(arr)
# arr.sort()
# print(arr)
# print(np.sort(arr))

# 多维数组排序
# arr = np.random.randint(0, 100, size=[3, 4])
# print(arr)
# 每一行 行内升序排序
# print(np.sort(arr))          # 按行排序
# print(np.sort(arr, axis=0))  # 按列排序

# 获得最小，最大的n个数，放到前面 ，但不排序

########################################################
# 级联(将两个数组拼接在一起)
# 一维数组
"""
arr1 = np.random.randint(0, 100, 5)
arr2 = np.random.randint(0, 100, 5)

print(arr1)
print(arr2)
print(np.concatenate((arr1, arr2)))
"""

# 二维数组
"""
arr1 = np.random.randint(0, 100, size=[4, 3])
arr2 = np.random.randint(0, 100, size=[4, 3])
print(arr1)
print(arr2)
print(np.concatenate((arr1, arr2)))  # 上下拼
print(np.concatenate((arr1, arr2), axis=1))  # 左右拼
# 维度不一样不能级联   例：一个size=[3, 4]另一个size = [3, 3]
"""
#########################################################
# 数组分割
"""
arr1 = np.random.randint(0, 100, size=[4, 3])
arr2 = np.random.randint(0, 100, size=[4, 3])
# 横着切
print(np.vsplit(arr1, indices_or_sections=2))   # 后一个参数是步长
# 竖着切
print(np.hsplit(arr1, indices_or_sections=3))   # 后一个参数是步长
"""
# 复制
# 别名
arr1 = np.random.randint(0, 100, size=[4, 3])

print(arr1)
arr2 = arr1.copy()
arr2[0, 0] = 1000
print(arr2)
print(arr1)











