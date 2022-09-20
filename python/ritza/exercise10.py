# 1. Add some new key bindings to the first sample program:
# - Pressing keys R, G or B should change tess’s color to Red, Green or Blue.
# - Pressing keys + or - should increase or decrease the width of tess’s pen. Ensure that the pen size
# stays between 1 and 20 (inclusive).
# - Handle some other keys to change some attributes of tess, or attributes of the window, or to give
# her new behaviour that can be controlled from the keyboard

import turtle # tess becomes a traffic light


def draw_housing():
    """Draw a housing to hold the traffic light"""
    tess.pensize(3)
    tess.color('black', 'darkgrey')
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


def advance_state_machine():
    global state_num
    if state_num == 0:
        tess.forward(70)
        tess.fillcolor('orange')
        state_num = 1
    elif state_num == 1:
        tess.forward(70)
        tess.fillcolor('red')
        state_num = 2
    else:
        tess.back(140)
        tess.fillcolor('green')
        state_num = 0
    # exercise - number 2
    wn.ontimer(advance_state_machine, 2000)


def change_color_r():
    tess.fillcolor('Red')


def change_color_g():
    tess.fillcolor('Green')


def change_color_b():
    tess.fillcolor('Blue')


def increase_pensize():
    global state_pensize
    if state_pensize < 20:
        state_pensize += 1
        print('pensize increase into:', state_pensize)
    else:
        print('current state', state_pensize, ', pensize cannot above 20 unit')


def decrease_pensize():
    global state_pensize
    if state_pensize > 1:
        state_pensize -= 1
        print('pensize decrease into:', state_pensize)
    else:
        print('current state', state_pensize, ', pensize cannot below 1 unit')


turtle.setup(400, 500)
wn = turtle.Screen()
wn.title('Tess becomes a traffic light!')
wn.bgcolor('lightgreen')
tess = turtle.Turtle()

draw_housing()

tess.penup()
tess.forward(40)
tess.left(90)
tess.forward(50)

tess.shape('circle')
tess.shapesize(3)
tess.fillcolor('green')

state_num = 0
# exercise - number 1
state_pensize = 1

# wn.onkey(advance_state_machine, 'space')
# exercise - number 1
wn.onkey(change_color_r, 'r')
wn.onkey(change_color_g, 'g')
wn.onkey(change_color_b, 'b')
wn.onkey(increase_pensize, '+')
wn.onkey(decrease_pensize, '-')
# exercise - number 2
advance_state_machine()

wn.listen()
wn.mainloop()

#note
# i skipped these exercise on purpose because i wanna learn about 
# OOP using py



# 3. In an earlier chapter we saw two turtle methods, hideturtle and showturtle that can hide or show
# a turtle. This suggests that we could take a different approach to the traffic lights program. Add to
# your program above as follows: draw a second housing for another set of traffic lights. Create three
# separate turtles to represent each of the green, orange and red lights, and position them appropriately
# within your new housing. As your state changes occur, just make one of the three turtles visible at
# any time. Once you’ve made the changes, sit back and ponder some deep thoughts: you’ve now got
# two different ways to use turtles to simulate the traffic lights, and both seem to work. Is one approach
# somehow preferable to the other? Which one more closely resembles reality – i.e. the traffic lights
# in your town?
# 4. Now that you’ve got a traffic light program with different turtles for each light, perhaps the
# visibility / invisibility trick wasn’t such a great idea. If we watch traffic lights, they turn on and off
# – but when they’re off they are still there, perhaps just a darker color. Modify the program now so
# that the lights don’t
# disappear: they are either on, or off. But when they’re off, they’re still visible.
# 5. Your traffic light controller program has been patented, and you’re about to become seriously rich.
# But your new client needs a change. They want four states in their state machine: Green, then Green
# and Orange together, then Orange only, and then Red. Additionally, they want different times spent
# in each state. The machine should spend 3
# seconds in the Green state, followed by one second in the Green+Orange state, then one second in
# the Orange state, and then 2 seconds in the Red state. Change the logic in the state machine.
# 6. If you don’t know how tennis scoring works, ask a friend or consult Wikipedia. A single game
# in tennis between player A and player B always has a score. We want to think about the “state of
# the score” as a state machine. The game starts in state (0, 0), meaning neither player has any score
# yet. We’ll assume the first element in this pair is the score for player A. If player A wins the first
# point, the score becomes (15, 0). If B wins the first point, the state becomes (0, 15). Below are the first
# few states and transitions for a state diagram. In this diagram, each state has two possible outcomes
# (A wins the next point, or B does), and the uppermost arrow is always the transition that happens
# when A wins the point. Complete the diagram, showing all transitions and all states. (Hint: there
# are twenty states, if you include the duece state, the advantage states, and the “A wins” and “B wins”
# states in your diagram.