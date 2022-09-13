# # 8. Comparison Operators
import numpy as np

# print(2 < 3)
# print('Alan' < 'Alin')
# print(3 < 'Alin')

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
# print(bmi)
# print(bmi > 23)
# print(bmi[bmi > 23])


# # 9. Boolean Operators
# True & False & not
# x = 12
# print(x > 5 and x < 15)
# print(not True)

# print(bmi > 21 and bmi < 22) # error ambigous
# print(bmi[bmi > 21] and bmi[bmi < 22]) # error ambigous
# print(np.logical_and(bmi > 21, bmi < 22))
# print(bmi[np.logical_and(bmi > 21, bmi < 22)])