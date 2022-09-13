# # 12. While Loop
# error = 50

# while error > 1:
#     error /= 4
#     print(error)


# # 13. For Loop
# fam = [1.73, 1.68, 1.71, 1.89]

# for height in fam:
#     print(height)

# for index, height in enumerate(fam):
#     print(index, height)


# # 14. Looping Data Structures 1 (Dict, Numpy 2D)
# worlds = {'afganistan': 30.55, 'albania': 2.77, 'algeria': 39.21}
# for key, value in worlds:     # using method items cus too many values that trying to unpack
#     print(key + ' -- ' + str(value))

import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
# bmi = np_weight / np_height ** 2

# for val in bmi:
#     print(val)

# meas = np.array([np_height, np_weight])

# for val in meas:
#     print(val)

# for val in np.nditer(meas):     # unpack array 2d into per line
#     print(val)


# # 15. Looping Data Structures 2 (Pandas) 
import pandas as pd
new_df = pd.read_csv('d:/learning and code/python/niomic/Intermediate Python For Data Science/data.csv', index_col=0)
# print(new_df)

# for val in new_df:
#     print(val)

# for lab, row in new_df.iterrows():
#     print(lab)
#     print(row)

# for lab, row in new_df.iterrows():
#     print(lab + ': ' + row['capital'])

for lab, row in new_df.iterrows():
    new_df.loc[lab, 'panjang_karakter'] = len(row['country'])

print(new_df)