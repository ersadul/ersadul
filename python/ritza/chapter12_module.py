# # # 12.1. Random numbers
# # create a black box object that generates random number
import random 

# # rng = random.Random()
# # dice_throw = rng.randrange(1, 7) # return an integer from 1 untill 6
# # delay_in_seconds = rng.random()

# # print(rng.randrange(1, 100, 2))

# # cards = list(range(52))
# # rng.shuffle(cards)
# # print(cards)

# # 12.1.2. Picking balls from bags, throwing dice, shuffling a pack of
# # cards
# import random


# def make_random_ints(num, lower_bound, upper_bound):
#     """Generate a list containing num random ints between
#     lower_bound and upper_bound. upper_bound is an open bound"""
#     rng = random.Random() # create a random number generator 
#     result = []
#     for i in range(num):
#         result.append(rng.randrange(lower_bound, upper_bound))
#     return result
# print(make_random_ints(5, 1, 13))

# xs = list(range(1, 13))
# rng = random.Random()
# rng.shuffle(xs)
# result = xs[:5]
# print(result)

# import random

# def make_random_ints_no_dups(num, lower_bound, upper_bound):
#     """Generate a list containing num random between the parameter
#     the result list cannot contain duplicates"""
#     result = []
#     rng = random.Random()
#     for i in range(num):
#         while True:
#             candidate = rng.randrange(lower_bound, upper_bound)
#             if candidate not in result:
#                 break
#         result.append(candidate)
    
#     return result

# xs = make_random_ints_no_dups(5, 1, 10000000)
# print(xs)

# this method will not end 
# because the condition of while loop not break
# xs = make_random_ints_no_dups(10, 1, 6) 
# print(xs) 

# # 12.2. The time module
# import time

# def do_my_sum(xs):
#     sum = 0
#     for val in xs:
#         sum += val
#     return sum

# sz = 10000000
# testdata = range(sz)

# t0 = time.process_time()
# my_result = do_my_sum(testdata)
# t1 = time.process_time()
# print('my_result    = {0} (time taken = {1:.4f} second)'
#     .format(my_result, t1-t0))

# t2 = time.process_time()
# their_result = sum(testdata)
# t3 = time.process_time()
# print('their_result = {0} (time taken = {1:.4f} seconds)'
#     .format(their_result, t3-t2))

# # 12.3. The math module
# import math

# print(math.pi)
# print(math.e)
# print(math.sqrt(2.0))
# print(math.radians(90))
# print(math.sin(math.radians(90)))
# print(math.asin(1.0) * 2)


# # 12.4. Creating your own modules
# import seqtools
# s = 'A string!'
# print(seqtools.remove_at(4, s))

# # 12.5. Namespaces
# import Module1
# import Module2

# print(Module1.question)
# print(Module2.question)
# print(Module1.answer)
# print(Module2.answer)

# def f():
#     n = 7
#     print("printing n inside of f:", n)

# def g():
#     n = 42
#     print("printing n inside of g:", n)

# n = 11
# print("printing n before calling f:", n)
# f()
# print("printing n after calling f:", n)
# g()
# print("printing n after calling g:", n)


# # 12.6. Scope and lookup rules
# def range(n): # var n is local var namespace
#     return 123*n
# print(range(10))

# n = 10                # var n is globas var namespace
# m = 3                 # var m is globas var namespace
# def f(n):
#     m = 7             # var m and n here is local var namespace
#     return 2*n+m      
# print(f(5), n, m)

# # 12.7. Attributes and the dot operator
# Variables defined inside a module are called attributes of the module. We’ve seen that objects
# have attributes too: for example, most objects have a __doc__ attribute, some functions have
# a __annotations__ attribute. Attributes are accessed using the dot operator (.).


# # 12.8. Three import statement variants
# import math 
# x = math.sqrt(10)
# print(x)

# from math import cos, sin, sqrt
# x = sqrt(10)
# print(x)

# from math import *  # Import all the identifiers from math,
#                     # adding them to the current namespace.
# x = sqrt(10)        # Use them without qualification.
# print(x)

# import math as m
# print(m.pi)

# def area(radius):
#     import math
#     return math.pi * radius * radius
# x = math.sqrt(10) # This gives an error


# 12.9. Turn your unit tester into a module
# from unit_tester import test