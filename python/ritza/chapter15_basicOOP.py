# Chapter 15: Classes and Objects —
# the Basics

# 15.1. Object-oriented programming
# 15.2. User-defined compound data types

# class Point:
#     """Point class that represents and manipulate x,y coords"""

#     def __init__(self):
#         self.x = 0
#         self.y = 0

# p = Point() # instantiate an object of type Point
# q = Point()

# print(p, q)
# print(p.x, p.y, q.x, q.y) # print each value of Point


# 15.3. Attributes
# p.x = 3
# p.y = 4
# p.z = 0
# print(p.x, p.y, p.z)


# # 15.4. Improving our initializer
# class Point:
#     """Point class that represents and manipulate x, y coords"""

#     def __init__(self, x=0, y=0):
#         """Create a new point at x, y"""
#         self.x = x
#         self.y = y

# p = Point(1, 2)
# q = Point(3, 4)
# r = Point()
# print(p.x, q.y, r.x)


# # 15.5. Adding other methods to our class
# class Point:
#     """Point class that represents and manipulate x, y coords"""

#     def __init__(self, x=0, y=0):
#         """Create a new point at x, y"""
#         self.x = x
#         self.y = y

#     def distance_from_origin(self):
#         """Compute my distance from the origin"""
#         return ((self.x ** 2)  + (self.y ** 2) ) ** 0.5

# p = Point(3, 4)
# print(p.distance_from_origin())


# # 15.6. Instances as arguments and parameters
# class Point:
#     """Point class that represents and manipulate x, y coords"""

#     def __init__(self, x=0, y=0):
#         """Create a new point at x, y"""
#         self.x = x
#         self.y = y

#     def distance_from_origin(self):
#         """Compute my distance from the origin"""
#         return ((self.x ** 2)  + (self.y ** 2) ) ** 0.5
    
#     def print_point(point):
#         print('({0}, {1})'.format(point.x, point.y))

# p = Point(3, 4)
# p.print_point()


# # 15.7. Converting an instance to a string
# class Point:
#     """Point class that represents and manipulate x, y coords"""

#     def __init__(self, x=0, y=0):
#         """Create a new point at x, y"""
#         self.x = x
#         self.y = y

#     def to_string(self):
#         return '({0}, {1})'.format(self.x, self.y)

#     # add this function to modified return when we're going to print object of Point
#     def __str__(self):
#         return '({0}, {1})'.format(self.x, self.y)

# p = Point(3, 4)
# value_p = p.to_string()
# print(value_p)

# output: <__main__.Point object at 0x0000027763A80490> 
# print address of object in memory, before we add '__str__' function
# and changing into return value we want to show
# print(p)

# 15.8. Instances as return values
class Point:
    """Point class that represents and manipulate x, y coords"""

    def __init__(self, x=0, y=0):
        """Create a new point at x, y"""
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def halfway(self, target):
        """Return the halfway between myself and target"""
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    
def midpoint(p1, p2):
    """Return the midpoint of p1 and p2"""
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)

# p = Point(3, 4)
# q = Point(5, 12)
# r = midpoint(p, q)
# print(r)

# p = Point(3, 4)
# q = Point(5, 12)
# r = p.halfway(q)
# print(r)
# print(Point(3, 4).halfway(Point(5, 12)))

