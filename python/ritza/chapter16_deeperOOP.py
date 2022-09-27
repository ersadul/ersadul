# Chapter 16: Classes and Objects —
# Digging a little deeper
class Point:
    """Create a point"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

# 16.1. Rectangles
# class Rectangle:
#     """a class to manufacture rectangle objcts"""

#     def __init__(self, posn, w, h):
#         self.corner = posn
#         self.width = w
#         self.height = h
    
#     def __str__(self):
#         return '({0}, {1}, {2})'.format(self.corner, self.width, self.height)

# box = Rectangle(Point(0, 0), 100, 200)
# bomb = Rectangle(Point(100, 80), 5, 10)

# print('box:', box)
# print('bomb:', bomb)

# # 16.2. Objects are mutable
# class Rectangle:
#     """a class to manufacture rectangle objcts"""

#     def __init__(self, posn, w, h):
#         self.corner = posn
#         self.width = w
#         self.height = h
    
#     def __str__(self):
#         return '({0}, {1}, {2})'.format(self.corner, self.width, self.height)

#     def grow(self, delta_width, delta_height):
#         """ Grow this object by the deltas """
#         self.width += delta_width
#         self.height += delta_height
    
#     def move(self, dx, dy):
#         """Move this object by the deltas """
#         self.corner.x += dx
#         self.corner.y += dy

# r = Rectangle(Point(10,5), 100, 50)
# print(r)
# r.grow(25, -10)
# print(r)
# r.move(-10, 10)
# print(r)


# # 16.3. Sameness
# shallow equality
# p1 = Point(3, 4)
# p2 = Point(3, 4)
# print(p1 is p2)
# p3 = p1
# print(p1 is p3)

# deep equality
# def same_coordinates(p1, p2):
#     return (p1.x == p2.x) and (p1.y == p2.y)
# p1 = Point(3, 4)
# p2 = Point(3, 4)
# print(same_coordinates(p1, p2))

# Beware of ==
# p = Point(4, 2)
# s = Point(4, 2)
# print('== on Point returns', p == s)
# by default, == on object Point does a shallow equity test

# a = [2, 3]
# b = [2, 3]
# print('== on Point returns', a == b)
# by default, == do deep equity test on list


# # 16.4. Copying
import copy         # do copy of obj 
p1 = Point(3, 4)
p2 = copy.copy(p1)  # copy method just do shallow copy, not deep copy
print(p1 is p2)

# if we use deepcopy method. 
# it will not only copy the object, but also any embedded objects in obj too
b2 = copy.deepcopy(b1) 
