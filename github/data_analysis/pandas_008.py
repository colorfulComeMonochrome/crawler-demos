import pandas as pd

# 交叉表
table = pd.read_csv('datafile_5.txt')
print(table.head())

# print(table['addr'])
# print(table.addr)
# 最少要有两个参数  index  columns
# 若不指明values值  默认使用计数
# c_table = pd.crosstab(index=table['addr'], columns=table['sex'])
# c_table = pd.crosstab(index=table.addr, columns=table.sex)
# print(c_table)

# 若指定 values 值  需要制定处理函数 aggfunc
"""
c_table = pd.crosstab(index=table.addr,
                      columns=table.sex,
                      values=table.age,
                      aggfunc='mean')
print(c_table)
"""
# 多columns index
"""
c_table = pd.crosstab(index=[table.addr, table.married],
                      columns=table.sex,
                      values=table.age,
                      aggfunc='mean')
print(c_table)
"""
"""
c_table = pd.crosstab(index=table.addr,
                      columns=[table.sex, table.married],
                      values=table.age,
                      aggfunc='mean')
print(c_table)
"""
# margins=True/False 统计
"""
c_table = pd.crosstab(index=table.addr,
                      columns=table.sex,
                      values=table.age,
                      aggfunc='mean',
                      margins=True)
print(c_table)
"""
# 注意：values 不支持多个列

c_table = pd.crosstab(index=table.addr,
                      columns=[table.sex, 'age'],
                      values=table.age,     # 此处不能为列表，不允许
                      aggfunc='mean',)
print(c_table)


# 合并 需要用到add（加法）,注意与  join 数据结构上的区别
c_table_2 = pd.crosstab(index=table.addr,
                      columns=[table.sex, 'height'],
                      values=table.height,     # 此处不能为列表，不允许
                      aggfunc='mean',)
print(c_table_2)

print(pd.concat((c_table, c_table_2)))
print(c_table.add(c_table_2, fill_value=0))

# 交叉表保存格式有问题  需要使用xlsx
c_table.add(c_table_2, fill_value=0).to_excel('c_table.xlsx')









