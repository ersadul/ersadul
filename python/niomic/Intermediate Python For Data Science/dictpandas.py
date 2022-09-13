# # 6. Pandas 1 (Dict to DataFrame, CSV to DataFrame)
import pandas as pd
import numpy as np

data = {'country':['Brazil', 'Russia', 'India', 'China', 'South Africa'], 'capital' : ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'], 'area':[8.516, 17.10, 3.286, 9.597, 1.221], 'population':[200.4, 143.5, 1252, 1357, 52.98]}
df = pd.DataFrame(data)

# print(df) # print dataframe

# df.index = ['BR', 'RU', 'IN', 'CH', 'SA']
# print(df) # print dataframe with changed index 

# import file from 
new_df = pd.read_csv('d:/learning and code/python/niomic/Intermediate Python For Data Science/data.csv', index_col=0)
# print(new_df)


# # 7. Pandas 2 (Square Bracket, Loc & Iloc)
# print(new_df['country'])           # print df with typedata
# print(new_df[['country']])         # print only df
# print(new_df[['country','population','area']])
# print(new_df[1:4])                 # print row in range condition

# print(new_df.loc['RU'])
# print(new_df.loc[['RU', 'CH']])
# print(new_df.loc[['RU', 'CH'], ['country', 'capital']])

# print(new_df.iloc[[1,0]])
# print(new_df.iloc[[1,0,2], [0,1]])


# # 11. Filtering Pandas DataFrame
# # print area above value '8'
# print(new_df['area'])
# print(new_df['area'] > 8)


# is_huge = new_df['area'] > 8
# print(is_huge)
# print(new_df[is_huge])

# # print area within certain range
# np.logical_and(new_df['area'] > 8, new_df['area'] < 10)
# print(new_df[np.logical_and(new_df['area'] > 8, new_df['area'] < 10)])