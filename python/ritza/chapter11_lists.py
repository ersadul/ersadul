# # 11.1. List values
# ps = [10, 20, 30, 40] 
# qs = ['spam', 'bungee', 'swallow']
# print(ps, qs)

# # 11.2. Accessing elements
# number = [i for i in range(10) ]
# print(number[0])
# print(number[2])

# horsemen = ['war', 'famine', 'pestilence', 'death']
# for i in [0, 1, 2, 3]:
#     print(horsemen[i])

# for h in horsemen:
#     print(h)

# # 11.3. List length
# horsemen = ['war', 'famine', 'pestilence', 'death']
# for i in range(len(horsemen)):
#     print(horsemen[i])

# print(len(["car makers", 1, ["Ford", "Toyota", "BMW"], [1, 2, 3]]))

# # 11.4. List membership
# horsemen = ['war', 'famine', 'pestilence', 'death']
# print('pestilence' in horsemen)
# print('debauchery' in horsemen)
# print('debauchery' not in horsemen)

# students = [
# ("John", ["CompSci", "Physics"]),
# ("Vusi", ["Maths", "CompSci", "Stats"]),
# ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
# ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
# ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

# counter = 0
# for (name, subject) in students:
#     if 'CompSci' in subject:
#         counter += 1
# print("The number of students taking CompSci is", counter)

# # 11.5. List operations
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# print([0] * 4)
# print([1, 2, 3] * 3)

# # 11.6. List slices
# a_list = ["a", "b", "c", "d", "e", "f"]
# print(a_list[1:3])
# print(a_list[:4])
# print(a_list[3:])
# print(a_list[:])

# # 11.7. Lists are mutable
# fruit = ["banana", "apple", "quince"]
# fruit[0] = 'pear'
# fruit[2] = 'orange'
# print(fruit)

# my_string = 'test'
# my_string[2] = 'x' # error
# print(my_string)

# a_list = ["a", "b", "c", "d", "e", "f"]
# a_list = []
# print(a_list)

# # 11.8. List deletion
# a = ["one", "two", "three"]
# del a[1]
# print(a)

# a_list = ["a", "b", "c", "d", "e", "f"]
# del a_list[1:5]
# print(a_list)

# 11.9. Objects and references
# a = 'banana'
# b = 'banana'
# print(a is b) 
# python refer two different object 
# to the same value, because strings are immutable and
# python optimize the resource to save in the memory

# a  = [1, 2, 3]
# b  = [1, 2, 3]
# print(a == b)
# print(a is b)
# in list case is different, a and b have same value 
# but not same object

# # 11.10. Aliasing
# a = [1, 2, 3]
# b = a
# print(a is b)

# # 11.11. Cloning lists
# a = [1, 2, 3]
# b = a[:]
# print(a is b)

# # 11.12. Lists and for loops
# friends =  ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
# for friend in friends:
#     print(friend)

# for num in range(20):
#     if num % 3 == 0:
#         print(num)

# for fruit in  ["banana", "apple", "quince"]:
#     print("I like to eat " + fruit + "s!")

# xs = [1, 2, 3, 4, 5]
# for i in range(len(xs)):
#     xs[i] = xs[i] ** 2
# print(xs)

# xs = [1, 2, 3, 4, 5]
# for (i, val) in enumerate(xs):
#     xs[i] = val ** 2
# print(xs)

# for i, val in enumerate(["banana", "apple", "pear", "lemon"]):
#     print(i, val)

# # 11.13. List parameters
# def double_stuff(a_list):
#     """Overwrite each element in a_list with double its value"""
#     for i, val in enumerate(a_list):
#         a_list[i] = 2 * val

# things = [2, 5, 9]
# double_stuff(things)
# print(things)
    
# # 11.14. List methods
# mylist = []
# mylist.append(5)
# mylist.append(27)
# mylist.append(3)
# mylist.append(12)
# print(mylist)

# mylist.insert(1, 12)
# print(mylist)

# mylist.extend([5, 9, 5, 11])
# print(mylist)

# print(mylist.index(9))

# mylist.reverse()
# print(mylist)

# mylist.sort()
# print(mylist)

# mylist.remove(12)
# print(mylist)

# # 11.15. Pure functions and modifiers
# def double_stuff(a_list):
#     """Return a new list which contains 
#     doubles of the elements in a_list"""
#     new_list = []
#     for val in a_list:
#         elem = 2 * val
#         new_list.append(elem)
    
#     return new_list
# things = [2, 5, 9]
# xs = double_stuff(things)
# print(xs)

# # 11.16. Functions that produce lists
def primes_lessthan(n):
    """Return a list of all prime numbers less than n"""
    result = []
    for i in range(2, n):
        if is_prime():
            result.append(i)
    return result

# # 11.17. Strings and lists
# song = 'The rain in spain...'
# words = song.split()
# print(words)

# # delimiter
# print(song.split('ai'))

# glue =';'
# s = glue.join(words)
# print(s)
# print('---'.join(words))
# print(''.join(words))

# # 11.18. list and range
# xs = list('Crunchy Frog')
# print(xs)
# print(''.join(xs))

# def f(n):
#     """Find the first positive integer between 101
#     and less than n that is divisible by 21"""
#     for i in range(101, n):
#         if i % 21 == 0:
#             return i

# import sys

# def test(did_pass):
#     """ Print the result of a test. """
#     linenum = sys._getframe(1).f_lineno
#     if did_pass:
#         msg = 'Test at line {0} ok.'.format(linenum)
#     else:
#         msg = 'Test at line {0} failed.'.format(linenum)
#     print(msg)


# def test_suite():
#     """ Run the suite of test for code in this module. """
#     test(f(110) == 105)
#     test(f(1000000000) == 105)

# test_suite()

# # 11.19. Nested lists
# nested = ["hello", 2.0, 5, [10, 20]]
# print(nested[3])

# elem = nested[3]
# print(elem[0])

# # 11.20. Matrices
# mx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(mx[1][2])