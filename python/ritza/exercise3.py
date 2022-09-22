# # 1. Write a program that prints We like Python's turtles! 1000 times.
# for i in range(1000):
#     print("We like Python's turtles!")


# # 2. Give tess[i] attributes of your cellphone object. Give tess[i] methods of your cellphone.


# # 3. Write a program that uses a for loop to print
# for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'October','September', 'Nopember', 'December']:
#     print('One of the months of the year is',month)


# # 4. Suppose our turtle tess is at heading 0 — facing east. We execute the statement tess.left(3645). What does tess do, and what is her final heading?
# import turtle

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.shape("turtle")
# tess.color("blue")
# tess.left(3645)

# wn.mainloop()


# 5. Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# a. Write a loop that prints each of the numbers on a new line.
# b. Write a loop that prints each number and its square on a new line.
# c. Write a loop that adds all the numbers from the list into a variable called total. You should
# set the total variable to have the value 0 before you start adding them up, and print the value
# in total after the loop has completed.

# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# # a.
# for number in xs:
#     print(number)
# # b.
# for number in xs:
#     print(number**2)
# # c.
# total = 0
# for number in xs:
#     total += number
# print(total)
# # d.
# total = 1
# for number in xs:
#     total *= number
# print(total)


# 6. Use for loops to make a turtle draw these regular polygons (regular means all sides the same
# lengths, all angles the same):
# - An equilateral triangle
# - A square
# - A hexagon (six sides)
# - An octagon (eight sides)

# import turtle

# wn = turtle.Screen()
# wn.bgcolor("white")
# tess = turtle.Turtle()
# tess.shape("turtle")
# tess.color("black")

# for i in range(3):
#     tess.forward(50)
#     tess.left(120)

# for i in range(4):
#     tess.forward(50)
#     tess.left(90)

# for i in range(6):
#     tess.left(60)
#     tess.forward(50)

# for i in range(8):
#     tess.left(45)
#     tess.forward(50)

# wn.mainloop()


# 7. A drunk pirate makes a random turn and then takes 100 steps forward, makes another random
# turn, takes another 100 steps, turns another random amount, etc. A social science student
# records the angle of each turn before the next 100 steps are taken. Her experimental data is
# [160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive angles are counter-clockwise.)
# Use a turtle to draw the path taken by our drunk friend.

# 8. Enhance your program above to also tell us what the drunk pirate’s heading is after he has
# finished stumbling around. (Assume he begins at heading 0).

# import turtle
# import random

# screen = turtle.Screen()
# tess = turtle.Turtle()

# rand_angle = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# for i in range(100):
#     direction = rand_angle[random.randint(0, 8)]
#     if direction > 0:
#         tess.left(direction)
#     else:
#         tess.right(direction)
#     tess.forward(100)

#     if i == 99:
#         print(direction)

# screen.mainloop()


# random pirate and back to the place
# import random

# tess = turtle.Turtle()

# direc = []
# step = []
# step_list = [20, 15, 24, 50, 35, 10]
# move = 0
# for i in range(10):
#     if move == 5:
#         move = 0
#     direc.append(random.choice(step_list))
#     step.append(random.choice(step_list))
#     tess.left(direc[i])
#     tess.forward(step[i])
#     move += 1
# print(step, direc)
# direc.reverse()
# step.reverse()
# print(step, direc)

# for i in range(10):
#     if move == 5:
#         move = 0
#     tess.back(step[i])
#     tess.right(direc[i])
#     move += 1

# turtle.mainloop() 

# 9. If you were going to draw a regular polygon with 18 sides, what angle would you need to turn
# the turtle at each corner?

# import turtle

# tess = turtle.Turtle()
# tess.hideturtle()

# for i in range(18):    
#     tess.forward(50)
#     tess.left(20)

# turtle.mainloop()


# 10. At the interactive prompt, anticipate what each of the following lines will do, and then record
# what happens. Score yourself, giving yourself one point for each one you anticipate correctly:

# 1 >>> import turtle
# 2 >>> wn = turtle.Screen()
# 3 >>> tess = turtle.Turtle()
# 4 >>> tess.right(90)
# 5 >>> tess.left(3600)
# 6 >>> tess.right(-90)
# 7 >>> tess.speed(10)
# 8 >>> tess.left(3600)
# 9 >>> tess.speed(0)
# 10 >>> tess.left(3645)
# 11 >>> tess.forward(-100)


# 11. Write a program to draw a shape like this:
# import turtle
# wn = turtle.Screen()
# tess = turtle.Turtle()
# tess.hideturtle()

# tess.left(36)

# for i in range(2):
#     tess.forward(50)
#     tess.right(36)
#     tess.backward(50)
#     tess.right(36)

# tess.forward(50)
# turtle.mainloop()

# 12. Write a program to draw a face of a clock that looks something like this:
# import turtle

# wn = turtle.Screen()
# center = turtle.Turtle()
# center.shape('turtle')

# tess = []
# angle = 0
# for i in range(12):
#     tess.append(turtle.Turtle())
#     tess[i].speed(0)
#     tess[i].shape('turtle')
#     tess[i].right(angle)
#     tess[i].penup()
#     tess[i].forward(140)
#     tess[i].pendown()
#     tess[i].forward(10)
#     tess[i].penup()
#     tess[i].forward(20)
#     tess[i].stamp()
#     angle += 30

# turtle.mainloop()


# 13. Create a turtle, and assign it to a variable. When you ask for its type, what do you get?
# import turtle

# var = turtle.Turtle() 
# print(type(var)) # <class 'turtle.Turtle'>


# 14. What is the collective noun for turtles? (Hint: they don’t come in herds.)
# import turtle

# tesses = turtle.turtles()
# print(type(tesses)) # <class 'list'>


# 15. What the collective noun for pythons? Is a python a viper? Is a python venomous?
