# # Chapter 19: Exceptions
# 19.1. Catching exceptions
# print(55/0)

# a = []
# print(a[5])
# tup = ("a", "b", "d", "d")
# tup[2] = "c"

# filename = input('Enter a filename:')
# try:
#     f = open(filename, 'r')
# except:
#     print('There is no file named', filename)

# def exist(filename):
#     try:
#         f = open(filename)
#         f.close()
#         return True
#     except:
#         return False
# print(exist('s'))

# A template to test if a file exists, without using exceptions
# import os
# # this is preferred way to check if a file exist or not!
# if os.path.isfile('D:\\learning and code\\python\\ritza\\chapter19_exception.py'):
#     is_exist = True
# else:
#     is_exist = False
# print(is_exist)

# 19.2. Raising our own exceptions
# def get_age():
#     age = int(input('please enter your age:'))
#     if age < 1:
#         raise ValueError('{0} is not a valid age'.format(age))
# print(get_age())

# 19.3. Revisiting an earlier example
# def recursion_depth(number):
#     print('recursion depth number', number)
#     try:
#         recursion_depth(number+1)
#     except:
#         print('I cannot go any deeper into the wormhole.')
# recursion_depth(0)

# 19.4. The finally clause of the try statement
# import turtle
# import time

# def show_poly():
#     try:
#         win = turtle.Screen() #grab/create a resource 
#         tess = turtle.Turtle()

#         n = int(input('How many sides do you want in your polygon?'))
#         angle = 360 / n
#         for i in range(n):
#             tess.forward(10)
#             tess.left(angle)
#         time.sleep(3)
#     finally:
#         win.bye()

# show_poly()

# 1. Write a function named readposint that uses the input dialog to prompt the user for a positive
# integer and then checks the input to confirm that it meets the requirements. It should be able to handle
# inputs that cannot be converted to int, as well as negative ints, and edge cases (e.g. when the user
# closes the dialog, or does not enter anything at all.)
def readposint():
    import tkinter as tk
    from tkinter import simpledialog

    try:
        ROOT = tk.Tk()
        ROOT.withdraw()
        # the input dialog
        user_input = int(simpledialog.askstring(title="Test",
            prompt="Enter a positive number?:"))
        if user_input < 0:
            raise ValueError(f'number you given is negative: {user_input}')
        
        return user_input

    except TypeError:
        raise TypeError('you must input number')
    except ValueError:
        raise ValueError(f'number you given is negative: {user_input}')
    
print(readposint())