# # Keypress events
# import turtle

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title('Handling keypresses!')
# tess = turtle.Turtle()

# def h1():
#     tess.forward(30)

# def h2():
#     tess.left(45)

# def h3():
#     tess.right(45)

# def h4():
#     wn.bye()

# wn.onkey(h1, 'Up')
# wn.onkey(h2, 'Left')
# wn.onkey(h3, 'Right')
# wn.onkey(h4, 'q')

# # Now we need to tell the window to start listening for events,
# # If any of the keys that we're monitoring is pressed, its
# # handler will be called.
# wn.listen()
# wn.mainloop()

# # # Keypress events
# import turtle

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title('How to handle mouse clicks on the window!')

# tess = turtle.Turtle()
# tess.pensize(3)
# tess.shape('circle')


# def h1(x, y):
#     wn.title('Got click at coords {0}, {1}'.format(x, y))
#     tess.goto(x, y)

# wn.onclick(h1)
# wn.mainloop()

# # Handler for 2 instances
# import turtle

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title('Handling mouse clicks!')
# tess = turtle.Turtle()
# tess.color('red')
# alex = turtle.Turtle()
# alex.color('blue')
# alex.forward(100)

# def handler_for_tess(x, y):
#     wn.title('Tess clicked at {0}, {1}'.format(x, y))
#     tess.left(42)
#     tess.forward(30)

# def handler_for_alex(x, y):
#     wn.title('Alex clicked at {0}, {1}'.format(x, y))
#     alex.right(84)
#     alex.forward(50)

# tess.onclick(handler_for_tess)
# alex.onclick(handler_for_alex)

# wn.mainloop()

import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title('using a timer')

tess = turtle.Turtle()
tess.color('blue')
tess.pensize(3)

def h1():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h1, 2000)

h1()
wn.mainloop()