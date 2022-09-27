# # 16.6. Exercises
from unit_tester import test

class Point:
    """Create a point"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

class Rectangle:
    """a class to manufacture rectangle objcts"""

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)
    
    def flip(self):
        """Flip the value between width and height"""
        self.width, self.height = self.height, self.width
    
    def contains(self, point):
        if ((point.x >= self.corner.x) and (point.x < self.width)) and \
            ((point.y >= self.corner.y) and (point.y < self.height)):
            return True
        return False
    
def is_collide():
    
    pass

# 1. Add a method area to the Rectangle class that returns the area of any instance:
# r = Rectangle(Point(0, 0), 10, 5)
# test(r.area() == 50)

# 2. Write a perimeter method in the Rectangle class so that we can find the perimeter of any rectangle
# instance:
# r = Rectangle(Point(0, 0), 10, 5)
# test(r.perimeter() == 30)

# 3. Write a flip method in the Rectangle class that swaps the width and the height of any rectangle
# instance:
# r = Rectangle(Point(100, 50), 10, 5)
# test(r.width == 10 and r.height == 5)
# r.flip()
# test(r.width == 5 and r.height == 10)

# 4. Write a new method in the Rectangle class to test if a Point falls within the rectangle. For this
# exercise, assume that a rectangle at (0,0) with width 10 and height 5 has open upper bounds on the
# width and height, i.e. it stretches in the x direction from [0 to 10), where 0 is included but 10 is
# excluded, and from [0 to 5) in the y direction. So it does not contain the point (10,2). These tests
# should pass:
# r = Rectangle(Point(0, 0), 10, 5)
# test(r.contains(Point(0, 0)))
# test(r.contains(Point(3, 3)))
# test(not r.contains(Point(3, 7)))
# test(not r.contains(Point(3, 5)))
# test(r.contains(Point(3, 4.99999)))
# test(not r.contains(Point(-3, -3)))

# 5. In games, we often put a rectangular “bounding box” around our sprites. (A sprite is an object that
# can move about in the game, as we will see shortly.) We can then do collision detection between,
# say, bombs and spaceships, by comparing whether their rectangles overlap anywhere.
# i cant get the point, so i skipped this question