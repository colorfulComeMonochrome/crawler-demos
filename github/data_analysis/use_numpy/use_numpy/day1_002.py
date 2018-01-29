import numpy as np

# 矩阵：matrix
# 生成矩阵
# 注意矩阵的
# arr = np.array([1, 2, 3, 4])
# .dot()

# mat_1 = np.mat([1, 2, 3, 4])
# print(mat_1)
# print(type(mat_1))
#
# arr = np.random.randint(0, 100, size=[4, 3])
#
# print(arr)
# mat_1 = np.mat(arr)
# print(mat_1)


# mat_2 = np.mat(np.random.randint(0, 100, size=[3, 3]))

# 矩阵相乘
# print(mat_1.dot(mat_2))

# print(mat_1 * mat_2)


# 矩阵转置
arr = np.random.randint(0, 100, size=[4, 3])
mat_1 = np.mat(arr)
print(mat_1)
print(mat_1.T)

# 矩阵求逆(必须是方阵)(广义逆矩阵可以求逆)
mat_2 = np.mat(np.random.randint(0, 100, size=[3, 3]))
print(mat_2.I)















