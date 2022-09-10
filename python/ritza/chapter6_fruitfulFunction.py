# Chapter 6: Fruitful functions

# biggest = max(3, 7, 2)
# print(biggest)
# x = abs(3 - 11) + 10
# print(x)

# -----
# def area(radius):
#     return 3.14159 * radius**2
# print(area(7))

# # find absolute value of a variable
# def absolute_value(x):
#     if x < 0:
#         return -x
#     return x

# print(absolute_value(-5))

# -----
# # find first 2 letter word
# def find_first_2_letter_word(xs):
#     for word in xs:
#         if len(word) == 2:
#             return word
#     return 'none'

# print(find_first_2_letter_word(["This", "is", "a", "dead", "parrot"]))
# print(find_first_2_letter_word(["This", "its", "a", "dead", "parrot"]))

# -----
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dxsquared = dx*dx + dy*dy
#     return dxsquared ** 0.5


# -----
# # function to find area of circle
# import math

# def distance(x1, y1, x2, y2):
#     return math.sqrt( (x2 - x1)**2 + (y2 - x1)**2 )


# def area(radius):
#     return 3.14159 * radius**2


# def area2(xc, yc, xp, yp):
#     return area(distance(xc, yc, xp, yp))

# print(area2(1, 2, 6, 8))


# -----
# def is_devisible(x, y):
#     """Test if x is exactly divisible by y"""
#     return x % y == 0
    

# print(is_devisible(4, 2))


# -----
# unit testing 
import sys

def absolute_value(n):
    if n < 0:
        return -n
    return n


def absolute_value(n): # buggy version
    if n < 0:
        return 1
    elif n > 0:
        return n


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
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)


test_suite()


