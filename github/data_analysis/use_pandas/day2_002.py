import pandas as pd
import numpy as np


############################################
# DataFrame 相当于将一维的Series组合成一个二维的表格
# 默认索引
# data = np.random.randint(0, 100, size=[4, 4])
# df = pd.DataFrame(data=data)
# print(df)
# print(type(df))

# 自定义索引
# data = np.random.randint(0, 100, size=[4, 4])
# df = pd.DataFrame(data=data,
#                   index=['张三', '李四', '王五', '赵六'],
#                   columns=['Python', 'C++', 'PHP', 'Java'],
#         )
# print(df)

############################################################
# 通过索引获取数据
# 获得一列
# print(df['Python'])
# 获取的每一列都是一个序列
# print(type(df['Python']))
# 获取单列dataframe
# print(df[['Python']])

# 同时获得多列
# print(df[['C++', 'Python']])
# 获取多列就不是序列了,类型是dataframe
# print(type(df[['C++', 'Python']]))

# 同时限制 行和列 的索引
# 可以获取多行中的列
# print(df['C++'][['李四', '赵六']])
# 但是多列中的行不能如此获取
# print(df[['C++', 'Python']]['李四'])

# 通过ix、loc、iloc、values 获取行索引
# ix
# 单个中括号获取的是series
# print(df.ix['李四'])
# 两个中括号获取的是dataframe
# print(df.ix[['李四']])
# 也可以通过下标获取
# print(df.ix[2])
# print(df.ix[0, 2])
# print(df.ix[[0, 2]])

# loc
# 注意: loc不能通过数字下标获取行
# print(df.loc['李四'])
# print(df.loc[['李四']])
# print(df.loc[['李四'], ['C++']])

# iloc
# 注意：iloc不能通过文字下标获取行
# print(df.iloc[3])

# print(df.iloc[[0, 1], [1, 2]])

# values
# print(df.values)
# print(type(df.values))
# print(df.values[0, 1])

# DataFrame之间的运算
# data = np.random.randint(0, 100, size=[4, 4])
# df1 = pd.DataFrame(data=data,
#                   index=['张三', '李四', '王五', '赵六'],
#                   columns=['Python', 'C++', 'PHP', 'Java'],
#         )
# print(df1)
# data = np.random.randint(0, 100, size=[4, 3])
# df2 = pd.DataFrame(data=data,
#                   index=['张三', '李四', '王五', '赵6'],
#                   columns=['Python', 'C++', 'Java'],
#         )
# print(df2)

# print(df1 + df2)
# print(df1 * df2)

# 不同维度运算
# print(df1 + df2)
# print(df1.add(df2, fill_value=0))

# 合并
# 上下拼接
# 维度不一样可以自动用nan填充
# print(pd.concat((df1, df2)))
# 左右拼接
# print(pd.concat((df1, df2), axis=1))

# 可以拼接多个
# print(pd.concat((df1, df2, df2), axis=0))
# print(pd.concat((df1, df2, df2), axis=1))

# 重建索引
# print(pd.concat((df1, df2), axis=0, ignore_index=True))
# print(pd.concat((df1, df2), axis=0, ignore_index=False))

# 拼接时加上二层索引
# 拼接几个dataframe 就加几个keys   keys少都不会报错   行列都可以
# print(pd.concat((df1, df2), axis=0, keys=['df1', 'df2', 'df3']))
# print(pd.concat((df1, df2), axis=1, keys=['df1', 'df2', 'df3']))


#####################################################
# 多层索引
data = np.random.randint(0, 100, size=[4, 8])
df1 = pd.DataFrame(data=data,
                  index=[['一班', '一班', '二班', '二班'], ['张三', '李四', '王五', '赵六']],
                  columns=[['期中', '期中', '期中', '期中', '期末', '期末', '期末', '期末'],
                           ['Python', 'C++', 'PHP', 'Java', 'Python', 'C++', 'Java', 'PHP']],)
# print(df1)


###########################################################
# stack 和 unstack  实现行列转换
# stack column转换
# print(df1)
# print(df1.stack(level=0))
# print(df1.stack(level=1))

# unstack index转换
# df2 = df1.unstack(level=0)
# print(df2)
# print(df2.unstack())

# 聚合操作
# print(df1)
# print(df1.sum())
# print(df1.sum(axis=1))

##############################################
# 从csv文件录入数据
# table = pd.read_csv('./state-abbrevs.csv')
# table = pd.read_csv('./datafile_1.txt', sep=',')
# print(table)
# 指定某列作为索引：index_col

############################################################
# merge级联
# 关联：不指定字段 则自动关联名字一样的
# table1 = pd.read_csv('./datafile_1.txt', sep=',')
# print(table1)
# table2 = table1.copy()
# table2.iloc[0,0] = '张3'
# print(table2)
# 内关联 ： 取交集    外关联： 并集
# print(table1.merge(table2, how='inner', on='Name', suffixes=('_1', '_2')))
# print(table1.merge(table2, how='outer', on='Name', suffixes=('_1', '_2')))

# 若字段名不一样,可以指定字段

# table2 = pd.read_csv('./datafile_1.txt.bak', sep=',')
# print(table1.merge(table2, how='inner', left_on='Name', right_on='Name1'))
# print(table1.merge(table2, how='inner'))
# print(table1.merge(table2, how='outer'))

# join 连接(关联)  join 和 concat一样，用索引关联
# 注意：lsuffix， rsuffix参数要写上
# print(table1.join(table2, lsuffix='_x', rsuffix='_y'))


# 数据去重
data = np.zeros((4, 3))
df = pd.DataFrame(data)
print(df)
# 去重函数
print(df.duplicated())    # 返回是否与第一行重复的bool值
print(df.drop_duplicates())  # 返回去重后的表格



















