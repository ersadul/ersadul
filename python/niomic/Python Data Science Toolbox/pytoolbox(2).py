# # Introduction to Iterators ( 1 )
# employees = ['Nick', 'Lore', 'Hugo']
# for employee in employees:
#     print(employee)

# for letter in 'Niomic':
#     print(letter)

# for i in range(4):
#     print(i)

# word = 'Da'
# it = iter(word)

# print(next(it))
# print(next(it))
# # print(next(it)) # error stop iteration

# use char '*' for word untill it ends
# word = 'Data'
# it = iter(word)
# print(*it)
# # print(*it) # and when we run it again, it will show nothing

# data = {'country':'Indonesia', 'capital':'Jakarta'}
# for i, n in data.items():
#     print(i, n)

# file = open('D:/learning and code/python/niomic/Python Data Science Toolbox/file.txt')
# it = iter(file)
# print(next(it))
# print(next(it))
# print(next(it))


# # Playing with iteratos (Enumerate & Zip) ( 2 )
# avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
# e = enumerate(avengers)
# print(type(e))
# e_list = list(e)
# print(e_list)

# for i, val in enumerate(avengers):
#     print(i, val)

# avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
# names = ['barton', 'stark', 'odison', 'maximoff']
# z = zip(avengers, names)
# print(type(z))
# z_list = list(z)
# print(z_list)

# for z1, z2 in zip(avengers, names):
#     print(z1, z2)

# # Using iterators to load large files into memory ( 3 )
# import pandas as pd

# # reading datasets without dividing into chunks
# df = pd.read_csv('D:/learning and code/python/niomic/Python Data Science Toolbox/data.csv')
# print(df.shape)
# print(df.info)

# # using chunksize to reading datasets and dividing datasets into chunks of data
# df = pd.read_csv('D:/learning and code/python/niomic/Python Data Science Toolbox/data.csv', chunksize=2)
# for i in df:
#     print(i.shape)
#     print(i.info)

# # Lists Comprehensions ( 4 )
# nums = [12, 8, 21, 3, 16]
# new_nums = []

# build list using for loop
# for num in nums:
#     new_nums.append(num +1)
# print(new_nums)

# build list using list comprehensions
# new_nums = [num + 1 for num in nums]
# print(new_nums)

# build list comprehensions using range method
# result = [num for num in range(11)]
# print(result)

# list comprehensions - nested loops
# pairs_1 = [(num1, num2) for num1 in range(0,2) for num2 in range(6,8)]
# print(pairs_1)


# # Advanced Comprehensions (Conditionals and Dictionaries) ( 5 )

# Conditionals in comprehensions
# print([num ** 2 for num in range(10) if num % 2 == 0]) # show num powered by 2 in range 0-9 when num mod 2 equal to 0
# print([num ** 2 if num % 2 == 0 else 0 for num in range(10)]) # show num powered by 2 if num mod 2 equal to 0, but if not show 0 when num in range from 0 till 9

# Dict Comprehensions
# pos_neg = {num: -num for num in range(9)}
# print(pos_neg)
# print(type(pos_neg))


# # Generator Expressions ( 6 )

# Printing Values From Generators (6.1)
# result = (num for num in range(6))
# print(list(result))

# Printing Values From Generators (6.2)
# result = (num for num in range(6))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result)) # error stop iterating

# print([num for num in range(10 ** 1000000)]) 
# if we run this line above, our session will be disconnected 
# cause the system performed operation was to resource-intensive


# the solution is using generator instead of list comprehensions
# print((num for num in range(10*1000000)))

# Conditionals in Generator Expressions (6.3)
# even_nums = (num for num in range(10) if num % 2 == 0)
# print(list(even_nums))

# Generator functions
# def num_sequence(n):
#     """Generate values from 0 to n"""
#     i = 0
#     while i <= n:
#         yield i
#         i += 1

# result = num_sequence(5)
# # print(type(result)) # object generator type
# for item in result:
#     print(item)

#---
# simpled version
# mygenerator = (x*x for x in range(3))
# for i in mygenerator:
#     print(i)

# detailed version. If you need more understanding, run this code in py visualizer
# def create_generator():
#     mylist = range(3)
#     for i in mylist:
#         yield i*i

# mygenerator = create_generator()
# print(mygenerator)
# for i in mygenerator:
#     print(i)
# ---

