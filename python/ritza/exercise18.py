# 18.8. Exercises
import turtle
from unit_tester import test
# 1. Modify the Koch fractal program so that it draws a Koch snowflake, like this:

# skip question until 4

# 5. Write a function, recursive_min, that
# returns the smallest value in a nested number list. Assume there
# are no empty lists or sublists:
# def recursive_min(lists):
#     mins = None
#     first = True

#     for elm in lists:
#         if type(elm) == type([]):
#             val = recursive_min(elm)
#         else:
#             val = elm

#         if first or val < mins:
#             mins = val
#             first = False
#     return mins
# test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
# test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
# test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
# test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

# 6. Write a function count that returns the number of occurrences of target in a nested list:
# def count(target, lists):
#     counter = 0
#     inlist = False

#     for elm in lists:
#         if type(elm) == type([]):
#             val = count(target, elm)
#             inlist = True
#         else:
#             val = elm

#         if inlist:
#             counter += val
#             inlist = False
#         elif val == target:
#             counter +=1
#     return counter 

# test(count(2, []) ==  0)
# test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
# test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
# test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
# test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
# test(count("a", [["this",["a",["thing","a"],"a"],"is"]
# , ["a","easy"]]) == 4)


# 7. Write a function flatten that returns a simple list containing all the values in a nested list:
# def flatten(lists):
#     result = []
#     in_list = False
#     for elm in lists:
#         if type(elm) == type([]):
#             val = flatten(elm)
#             in_list = True
#         else:
#             val = elm
        
#         if in_list:
#             for elm in val:
#                 result.append(elm)
#             in_list = False
#         else:
#             result.append(val)
#     return result

# test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
# test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
# test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
# test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
# ["this","a","thing","a","is","a","easy"])
# test(flatten([]) == [])

# 8. Rewrite the fibonacci algorithm without using recursion. Can you find bigger terms of the
# sequence? Can you find fib(200)? 173402521172797813159685037284371942044301
# def fib(n):
#     # 0,1,1,2,3,5,8,13,21
#     int1 = 1
#     int0 = 0
#     if n == 0:
#         return int0
#     elif n == 1:
#         return int1
#     for i in range(1,n-1):
#         temp = int0 + int1
#         int0 = int1 
#         int1 = temp
#     return int1
    
# print(fib(200)) # output: 173402521172797813159685037284371942044301

# 9. Use help to find out what sys.getrecursionlimit() and sys.setrecursionlimit(n) do. Create
# several experiments similar to what was done in infinite_recursion.py to test your understanding of how
# these module functions work.
# import sys 
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1000)
# print(sys.getrecursionlimit())


# 10. Write a program that walks a directory structure (as in the last section of this chapter), but
# instead of
# printing filenames, it returns a list of all the full paths of files in the directory or the
# subdirectories. (Don’t include directories in this list — just files.) For example, the output list
# might have elements like this:
# [“C:Python31Lib\site-packages\pygame\docs\ref\mask.html”,
# “C:Python31Lib\site-packages\pygame\docs\ref\midi.html”,
# …
# “C:Python31Lib\site-packages\pygame\examples\aliens.py”,
# …
# “C:Python31Lib\site-packages\pygame\examples\data\boom.wav”,
# … ]
# import os

# def print_filepath(path, prefix=''):
#     dirlist = os.listdir(path)
#     for element in dirlist:
#         fullpath = path + prefix + element 
#         if not os.path.isdir(path + element):
#             print(fullpath)
#         if os.path.isdir(fullpath):
#             print_filepath(fullpath, prefix='/')
    

# path = 'd:/learning and code/python/ritza/'
# # print(os.path.isdir(path+'Chapter 12'))
# # print(os.listdir(path))
# print_filepath(path)

# 11. Write a program named litter.py that creates an empty file named trash.txt in each
# subdirectory of a directory tree given the root of the tree as an argument (or the current directory as a default).
# Now write a program named cleanup.py that removes all these files.

# !!! not completed because the permission issue

# import os

# def make_trash_files(path, prefix='/'):
#     # with open('trash.txt', 'w') as file:
#     #     pass
#     dirlist = os.listdir(path)
#     for element in dirlist:
#         fullpath = path + prefix + element
#         print(fullpath)
#         with open(fullpath, 'w') as file:
#             file.write('')
#         if os.path.isdir(fullpath):
#             make_trash_files(fullpath, prefix='/')

# def del_trash_files(path):
#     pass

# path = 'D:/test1'
# make_trash_files(path)
# del_trash_files(path)
