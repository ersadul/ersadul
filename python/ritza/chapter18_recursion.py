# Chapter 18: Recursion
from unit_tester import test
import turtle

# def koch(t, order, size):
#     """Make turtle t draw a Koch fractal of 'order' and 
#     'size'. Leave the turtle facing the same direction."""
#     if order == 0:
#         t.forward(size)
#     else:
#         koch(t, order-1, size/3)
#         t.left(60)
#         koch(t, order-1, size/3)
#         t.right(120)
#         koch(t, order-1, size/3)
#         t.left(60)
#         koch(t, order-1, size/3)

# def koch2(t, order, size):
#     if order == 0:
#         t.forward(size)
#     else:
#         for angle in [60, -120, 60, 0]:
#             koch2(t, order-1, size/3)
#             t.left(angle)


# tess = turtle.Turtle()
# koch2(tess, 4, 250)

# turtle.mainloop()

# if we want to understand what kind of operation that 
# running in recursion we can devide that into chunks of
# function in more small way
# def koch_0(t, size):
#     t.forward(size)

# def koch_1(t, size):
#     for angle in [60, -120, 60, 0]:
#         koch_0(t, size/3)
#         t.left(angle)

# def koch_2(t, size):
#     for angle in [60, -120, 60, 0]:
#         koch_1(t, size/3)
#         t.left(angle)

# def koch_3(t, size):
#     for angle in [60, -120, 60, 0]:
#         koch_2(t, size/3)
#         t.left(angle)


# 18.2. Recursive data structures
# print(sum([1, 2, 8]))
# print(sum([1, 2, [11, 13], 8])) # error, cause func sum not support list as operand


#  18.3. Processing recursive number lists
# def r_sum(nested_num_list):
#     tot = 0
#     for element in nested_num_list:
#         if type(element) == type([]):
#             tot += r_sum(element)
#         else:
#             tot += element
#     return tot

# print(r_sum([1, 2, [11, 13], 8]))

# def r_max(nxs):
#     """Find the maximum value in a recursive structure of lists
#     within other lists.
#     Pre-condition: no lists or sublists are empty."""
#     largest = None 
#     # we add var first_time because operator in python 
#     # not support calculate between 'int' and 'None'
#     first_time = True                       
    
#     for e in nxs:
#         if type(e) == type([]):
#             val = r_max(e)
#         else:
#             val = e
        
#         # we use first_time variable to assign first var, 
#         # so we can operate with next value
#         if first_time or val > largest:
#             largest = val
#             # after the first value is set, that first_time var no longer used
#             first_time = False
#     return largest
#     # note: in some case we can use 0 as the largest, if we only calculate positif number
#     # so there is no reason we must use double var for supporting our function

# test(r_max([2, 9, [1, 13], 8, 6]) == 13)
# test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
# test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
# test(r_max(["joe", ["sam", "ben"]]) == "sam")


# 18.4. Case study: Fibonacci numbers
# import time

# def fib(n):
#     if n <= 1:
#         return n
#     t = fib(n-1) + fib(n-2)
#     return t

# t0 = time.time()
# n = 35
# result = fib(n)
# t1 = time.time()
# print('fib({0}) = {1}, ({2:.2f}) secs'.format(n, result, t1 - t0))


# 18.5. Example with recursive directories and files
# import os

# def get_dirlist(path):
#     """Return a sorted list of all entries in path. 
#     This returns just names, not the full patch to the names."""
#     dirlist = os.listdir(path)
#     dirlist.sort()
#     return dirlist

# def print_files(path, prefix = ''):
#     """Print recursive listing of contents of path"""
#     if prefix == '':    # detect outermost call, printing a heading
#         print('Folder listing for', path)
#         prefix = '/ '

#     dirlist = get_dirlist(path)
#     for f in dirlist:
#         print(prefix, f)    # print line
#         fullpath = os.path.join(path, f)    # turn into fullpath name
#         # fullpath = path + f
#         if os.path.isdir(fullpath):     # if directory recursive
#             print_files(fullpath, prefix + '/ ')

# path = 'd:/learning and code/python/ritza/'
# print_files(path)

# print(get_dirlist(path))
# print(path + 'hai')



