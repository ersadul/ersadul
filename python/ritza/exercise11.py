# 11.22. Exercises
import sys


def add_vectors(u, v):
    vector = []
    if len(u) == len(v):
        for i in range(len(u)):
            vector.append(u[i] + v[i])
    return vector


def scalar_mult(s, v):
    tmp = []
    for i in range(len(v)):
        new_list.append(s * v[i])
    return tmp


def dot_product(u, v):
    tmp = 0
    if len(u) == len(v):
        for i in range(len(u)):
            tmp += u[i] * v[i]
    return tmp

[
    [1, 2, 3],
    [2, 3, 1],
    [5, 1, 2]
]

def cross_product(u, v):
    tmp = []
    if len(u) == len(v):
        tmp.append(u[1] * v[2] - u[2] * v[1])
        tmp.append(u[2] * v[0] - u[0] * v[2])
        tmp.append(u[0] * v[1] - u[1] * v[0])
    return tmp


def replace(s, old, new):
    if len(old) == 1:
        words = [ch for ch in s]
        for i, word in enumerate(words):
            if word == old:
                words[i] = new

        return ''.join(words)

    else:
        words = s.split()
        for i, word in enumerate(words):
            if old in word:
                words[i] = word[:word.index(old)] + new + word[word.index(old)+len(old):]
                
        return ' '.join(words)


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
    # # 5. 
    # test(add_vectors([1, 1], [1, 1]) == [2, 2])
    # test(add_vectors([1, 2], [1, 4]) == [2, 6])
    # test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])    

    # # 6. 
    # test(scalar_mult(5, [1, 2]) == [5, 10])
    # test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    # test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    
    # # 7. 
    # test(dot_product([1, 1], [1, 1]) == 2)
    # test(dot_product([1, 2], [1, 4]) == 9)
    # test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    
    # # 8.
    # test(cross_product([1, 2, 3], [4, 5, 6]) == [-3, 6, -3])
    # test(cross_product([2, 1, 3], [1, 2, 5]) == [-1, -7, 3])

    # # 10.
    # test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    # s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    # test(replace(s, "om", "am") ==
    # "I love spam! Spam is my favorite food. Spam, spam, yum!")
    # test(replace(s, "o", "a") ==
    # "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

test_suite()


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

# 5. Lists can be used to represent mathematical vectors. In this exercise and several that follow you
# will
# write functions to perform standard operations on vectors. Create a script named vectors.py and
# write Python code to pass the tests in each case.
# Write a function add_vectors(u, v) that takes two lists of numbers of the same length, and returns
# a new list containing the sums of the corresponding elements of each:
# test(add_vectors([1, 1], [1, 1]) == [2, 2])
# test(add_vectors([1, 2], [1, 4]) == [2, 6])
# test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

# 6. Write a function scalar_mult(s, v) that takes a number, s, and a list, v and returns the scalar
# multiple¹⁰ of v by s:
# test(scalar_mult(5, [1, 2]) == [5, 10])
# test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
# test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

# 7. Write a function dot_product(u, v) that takes two lists of numbers of the same length, and returns
# the
# sum of the products of the corresponding elements of each (the dot_product¹¹).
# test(dot_product([1, 1], [1, 1]) == 2)
# test(dot_product([1, 2], [1, 4]) == 9)
# test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

# 8. Extra challenge for the mathematically inclined: Write a function cross_product(u, v) that
# takes two lists of numbers of length 3 and returns their cross product¹². You should write your own tests.

# 9. Describe the relationship between " ".join(song.split()) and song in the fragment of code
# below. Are they the same for all strings assigned to song? When would they be different?
# Answer: the are the same. it will be different when the character that used not ' '
# song = "The rain in Spain..."
# print(" ".join(song.split()))
# print((song.split()))

# 10. Write a function replace(s, old, new) that replaces all occurrences of old with new in a strings:
# test(replace("Mississippi", "i", "I") == "MIssIssIppI")
# s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
# test(replace(s, "om", "am") ==
# "I love spam! Spam is my favorite food. Spam, spam, yum!")
# test(replace(s, "o", "a") ==
# "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
# Hint: use the split and join methods.

# 11. Suppose you want to swap around the values in two variables. You decide to factor this out into a
# reusable function, and write this code:
# Answer: this function will not swap the value because value inside the function is not returned
# def swap(x, y): # Incorrect version
#     print("before swap statement: x:", x, "y:", y)
#     (x, y) = (y, x)
#     print("after swap statement: x:", x, "y:", y)

# a = ["This", "is", "fun"]
# b = [2,3,4]
# print("before swap function call: a:", a, "b:", b)
# swap(a, b)
# print("after swap function call: a:", a, "b:", b)

