import pandas as pd
import numpy as np

#############################
# Series 相当于有索引的一维数组,类似于python的字典
# 通过列表创建

# ser = pd.Series([1, 2, 3, 4])
# print(ser)
# print(ser[2])
# print(type(ser))

# 通过numpy数组创建
# arr = np.array([1, 2, 3, 4])
# ser = pd.Series(arr)
# print(ser)
# print(type(ser))

# 指定索引
# ser = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(ser)

# 通过Python字典创建,指定索引
# 字典索引不可以重复
# ser = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
# print(ser)
# 指定索引可以重复
# ser = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(ser)

# 通过索引获得或改变值
# print(ser['a'])


# 拷贝
# ser = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
# ser1 = ser.copy()
# ser1['a'] = 234
# print(ser)
# print(ser1)

###################################################################
# Series 的值，不只是数字，可以是多种多样
# ser = pd.Series({'a': 222, 'b': 'erfsa'})
# print(ser)

# 切片
# ser = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
# print(ser)
# print(ser['a':'c':2])

# 筛选
# ser = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
# print(ser[ser < 3])
# print(ser[ser == 10])


# 空值处理, 自动转换成NaN
# ser = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': None})
# print(ser)
# print(ser * 3)

# 序列间运算
# ser1 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': None})
# ser2 = pd.Series({'a': 1, 'b': 2, 'f': 3, 'd': None})
# print(ser1 + ser2)

# 序列间运算，用0替换nan
# print(ser1.add(ser2, fill_value=0))

# 序列多层索引
# ser = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# print(ser)

# ser = pd.Series([1, 2, 3, 4], index=[['a', 'b', 'c', 'd'], ['A', 'B', 'C', 'D']])
# print(ser)















