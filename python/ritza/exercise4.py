# #  1. Write a void (non-fruitful) function to draw a square. Use it in a program to draw the image
# #   shown below. Assume each side is 20 units. (Hint: notice that the turtle has already moved away
# #   from the ending point of the last square when the program ends.)
# import turtle

# def make_square(manySquare):
#     """
#     Turtle make a square or some square arranged from left to right
#     """
#     for i in range(manySquare):
#         for i in range(4):
#             tess.forward(20)
#             tess.left(90)
#         tess.penup()
#         tess.forward(40)
#         tess.pendown()

# wn = turtle.Screen()
# tess = turtle.Turtle()
# make_square(5)

# wn.mainloop()


# # 2. Write a program to draw this. Assume the innermost square is 20 units per side, and each
# # successive square is 20 units bigger, per side, than the one inside it.
# import turtle

# def make_square(manySquare):
#     """
#     Turtle make a square or some square that from small to big side 
#     which successive square is 20 units bigger than the smallest
#     """
#     tLength = 20
#     for i in range(manySquare):
#         for i in range(4):
#             tess.forward(tLength)
#             tess.left(90)
#         tess.penup()
#         tess.left(45)
#         tess.backward(14.5)
#         tess.right(45)
#         tess.pendown()

#         tLength += 20

# wn = turtle.Screen()
# tess = turtle.Turtle()
# make_square(5)

# wn.mainloop()


# # 3. Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon.
# # When called with draw_poly(tess, 8, 50), it will draw a shape like this:
# import turtle

# def draw_poly(t, n, sz):
#     """
#     Make a turtle t draw a regular polygon which have sides based on user input
#     """
#     angle = 360 / n
#     for i in range(n):
#         t.forward(sz)
#         t.left(angle)

# wn = turtle.Screen()
# tess = turtle.Turtle()
# draw_poly(tess, 10, 50)

# wn.mainloop()


# # 4. Draw this pretty pattern.
# import turtle
# import time

# def draw_polygon(t, poly):
#     """
#     Draw a regular polygon which looks like a sunflower? am i right stepsis? 
#     """
#     angle = 18
#     for i in range(poly):
#         t.forward(50)
#         t.left(90)
#         t.forward(50)
#         t.left(90)
#         t.forward(100)
#         t.left(90)
#         t.forward(100)
#         t.left(90)
#         t.forward(100)
#         t.left(90)
#         t.forward(50)
#         t.left(90)
#         t.forward(100)
#         t.backward(50)
#         t.left(90)
#         t.forward(50)
#         t.backward(100)
#         t.forward(50)
#         t.left(90)
#         t.left(angle)

# wn = turtle.Screen()
# wn.title('❤❤❤')
# tess = turtle.Turtle()
# tess.speed(7)
# tess.hideturtle()
# time.sleep(2)
# draw_polygon(tess, 5)
# tess.penup()
# tess.backward(50)
# tess.pendown()
# tess.backward(100)

# wn.mainloop()

# # 5. The two spirals in this picture differ only by the turn angle. Draw both.
# import turtle

# def draw_spiral(t, layer):
#     """
#     Make a spiral sided-corner that have 90 degree on every corner
#     """
#     tLength = 2
#     t.left(90)
#     t.backward(tLength)
    
#     for i in range(layer):
#         for j in range(2):
#             tLength += 4
#             t.right(90)
#             t.backward(tLength)
#             t.right(90)
#             t.backward(tLength)

# def draw_spiral_shuriken(t, layer):
#     """
#     Make a spiral that looks like a shuriken haha
#     """
#     tLength = 2
#     t.left(90)
#     t.backward(tLength)
    
#     for i in range(layer):
#         for j in range(2):
#             tLength += 4
#             t.right(90)
#             t.backward(tLength)
#             t.right(91)
#             t.backward(tLength)

# wn = turtle.Screen()

# tess = turtle.Turtle()
# tess.speed(0)
# tess.penup()
# tess.backward(150)
# tess.pendown()
# draw_spiral(tess, 25)

# alex = turtle.Turtle()
# alex.speed(0)
# alex.penup()
# alex.forward(150)
# alex.pendown()
# draw_spiral_shuriken(alex, 25)

# wn.mainloop()


# # 6. Write a void function draw_equitriangle(t, sz) which calls draw_poly from the previous
# # question to have its turtle draw a equilateral triangle.
# import turtle

# def draw_poly(t, n, sz):
#     """
#     Make a turtle t draw a regular polygon which have sides based on user input
#     """
#     angle = 360 / n
#     for i in range(n):
#         t.forward(sz)
#         t.left(angle)

# def draw_equitriangle(t, sz):
#     """
#     Draw a equilateral triangle from turtle t and side sz 
#     """
#     draw_poly(t, 3, sz)

# wn = turtle.Screen()
# tess = turtle.Turtle()
# draw_equitriangle(tess, 50)

# wn.mainloop()


# 7. Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and
# including n. So sum_to(10) would be 1+2+3…+10 which would return the value 55.

# def sum_to(n):
#     result = 0
#     for i in range(n+1):
#         result += i

#     return result

# print(sum_to(10))


# # 8. Write a function area_of_circle(r) which returns the area of a circle of radius r.
# import math

# def area_of_circle(r):
#     return math.pi*r*r

# print(math.ceil(area_of_circle(7)))


# # 9. Write a void function to draw a star, where the length of each side is 100 units. (Hint: You
# # should turn the turtle by 144 degrees at each point.)
# import turtle

# def draw_a_star():
#     """
#     Make turtle draw a star
#     """
#     for i in range(5):
#         for i in range(5):
#             tess.right(144)
#             tess.forward(100)
#         # tess.penup()
#         tess.forward(350)
#         tess.left(144)
#         # tess.pendown()
    
# wn = turtle.Screen()
# tess = turtle.Turtle()

# draw_a_star()

# wn.mainloop()