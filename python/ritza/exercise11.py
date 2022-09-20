# 11.22. Exercises
import sys


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} failed.'.format(linenum)
    print(msg)


def test_suite():
    """ Run the suite of test for code in this module. """


# 1. What is the Python interpreter’s response to the following?
# 1 >>> list(range(10, 0, -2))
# The three arguments to the range function are start, stop, and step, respectively. In this example,
# start is greater than stop. What happens if start < stop and step < 0? Write a rule
# for the relationships among start, stop, and step.
# answers:
# if start < stop and step < 0, the list that produce will be empty
# 1. if start < stop and step > 0, it will produce values from 'start' to 'stop - 1' and each step increase constantly as given number of 'step'
# 2. if start > stop and step < 0, it will produce values from 'start' to 'stop - 1' and each step decrease constantly as given number of 'step'
# 3. if start < stop and step < 0, it will produce empty values, in this case empty list
# 4. if start > stop and step > 0, it will produce empty values, in this case empty list
# print(list(range(1, 10, 1)))  # 1
# print(list(range(10, 0, -2))) # 2
# print(list(range(1, 10, -1))) # 3
# print(list(range(10, 1, 1)))  # 4


# 2. Consider this fragment of code:
# 1 import turtle
# 2
# 3 tess = turtle.Turtle()
# 4 alex = tess
# 5 alex.color("hotpink")

# Does this fragment create one or two turtle instances? Does setting the color of alex also change
# the color of tess? Explain in detail
# Answers:
# the fragmen of code above is creating one instance
# , because on the line 4. when we assign the variable tess into alex
# , it's just copying the object address from tess to alex. so, that two variable is referencing on the same object
# if we change color of alex or do anything about their attribute, of course the other one also changing 
# because they are referencing on the same object
# import turtle

# tess = turtle.Turtle()
# alex = tess
# alex.color("hotpink")
# # tess.forward(50)
# turtle.mainloop()

# # print(alex is tess) # output: true


# 3. Draw a state snapshot for a and b before and after the third line of the following Python code is
# executed:
# a = [1, 2, 3]
# b = a[:]
# print(a, b) # output: [1, 2, 3] [1, 2, 3]
# b[0] = 5
# print(a, b) # output: [1, 2, 3] [5, 2, 3]

# 4. What will be the output of the following program?
# Answer: even tho list 'this' and 'that' have a same value, they are literally different object
# because they instantiate value into different variable. and in test 1 surely the output is False, because they are not same obj
# and when we assign the variable 'this' into 'that', we copy the reference address. so the output of test 2 is True(same object)
# this = ["I", "am", "not", "a", "crook"]
# that = ["I", "am", "not", "a", "crook"]
# print("Test 1: {0}".format(this is that)) # output: Test 1: False
# that = this
# print("Test 2: {0}".format(this is that)) # output: Test 2: True
