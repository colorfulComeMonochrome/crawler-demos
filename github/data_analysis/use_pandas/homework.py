import numpy as np
import pandas as pd


table = pd.read_csv('datafile_4.txt', sep=',')
print(table.tail())


#######################################
# 1、获得2017年每个省份的利润率、员工人均利润
# table1 = table[table['年份'] == 2017]
# table1 = table1.groupby('省份')
# table1 = table1.sum()
# print(table1)
#
# profit_rate = table1['利润'] / (table1['营业额'] - table1['利润'])   # 省份利润率
# profit_person = table1['利润'] / table1['员工人数']
# print(profit_person)

# 2、分别获得 利润率 最高和最低的省份
# 通过排序获得
# table2 = table.groupby(by=('省份', '年份'))
# table2 = table2.sum()
# print(table2)
# table2['利润率'] = table2['利润'] / (table2['营业额'] - table2['利润'])
# print(table2)
# print(table2.sort_values(by='利润率'))
# 利润率最大最小值
# print(table2.max())
# print(table2.min())


# 利润率最大最小值对应的索引
# profit_rate = table2.sort_values(by='利润率')    # 利润率倒叙
# print(profit_rate)
# print(profit_rate.ix[0])    # 利润率最小值
# profit_rate = table2.sort_values(by='利润率', ascending=False)     # 利润率正序
# print(profit_rate.ix[0])    # 利润率最大值

# 通过索引获取一行
# print(profit_rate.ix['北京', 2016])


#######################################
# 3、获得2017年利润率相比2016年有所增长的城市
table3 = table.groupby(by=('省份', '年份'), as_index=False)
table3 = table3.sum()
table3['利润率'] = table3['利润'] / (table3['营业额'] - table3['利润'])
# print(table3)
table3_2016 = table3[table3['年份'] == 2016][['利润率', '省份']]
print(table3_2016)
table3_2017 = table3[table3['年份'] == 2017][['利润率', '省份']]

table3_up = table3_2016.merge(table3_2017, on='省份')
# print(table3_up)
print(table3_up[table3_up['利润率_x'] > table3_up['利润率_y']])
#####################################
# Mysql 实现以上逻辑




























