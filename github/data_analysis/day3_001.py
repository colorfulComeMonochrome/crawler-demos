import pandas as pd
import numpy as np
pop1 = pd.read_csv('./state-population.csv')
area = pd.read_csv('./state-areas.csv')
abb = pd.read_csv('./state-abbrevs.csv')


print(pop1.head())
print(area.head())
print(abb.head())

# 获得 2012 年各州的人口情况
# print(pop1[pop1['year'] == 2012])


# 获得 2010 年美国总人口
# print(pop1[(pop1['year'] == 2010) & (pop1['ages'] == 'total')])
# print(pop1[(pop1['year'] == 2010) & (pop1['ages'] == 'total')]['population'].sum())

# 获得 2010 年美国18岁以下总人口
# print(pop1[(pop1['year'] == 2010) & (pop1['ages'] == 'under18')]['population'].sum())

# 获得 2010 年美国18岁以下总人口 占 总人口比例
# under18 = pop1[(pop1['year'] == 2010) & (pop1['ages'] == 'under18')]['population'].sum()
# total = pop1[(pop1['year'] == 2010) & (pop1['ages'] == 'total')]['population'].sum()
# print('10年美国18岁以下总人口 占 总人口比例%.5f' % (under18 / total))


### 获得人口密度
# 美国 2012年 总人口密度
# population = pop1[(pop1['year'] == 2012) & (pop1['ages'] == 'total')]['population'].sum()
# areas = area['area'].sum()
# print(population / areas)
# 美国 2012年 各州总人口密度
# popu = pop1[(pop1['year'] == 2012) & (pop1['ages'] == 'total')]
# table = abb.merge(area, how='outer')
# print(table.head())
# popu = popu.rename(columns={'state/region': 'abbreviation'})
# print(popu.head())
# table = table.merge(popu, how='outer', on='abbreviation')
# print(table.head())
# table['per'] = table['population'] / table['area']
# print(table)


# AL州 各年份的人口密度
pop1 = pop1.rename(columns={'state/region': 'abbreviation'})
table = abb.merge(area, how='outer')
table = table.merge(pop1, how='outer')
table = table[table['abbreviation'] == 'AL']
table['per'] = table['population'] / table['area']
print(table)

# drop : 删除无用的列，inplace=True表示在原表上操作，否则会返回一个新表













