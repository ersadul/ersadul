# # function to make square with turtle
# import turtle

# def draw_square(t, sz):
#     """
#     Function to make a square 
#     where t for a turtle object and sz for size of square
#     """

#     for i in range(4):
#         t.forward(sz)
#         t.left(90)

# wn = turtle.Screen()
# wn.title('Alex learn how to use function')

# alex = turtle.Turtle()
# draw_square(alex, 50)
# print(draw_square.__doc__)
# wn.mainloop()

# # function to make multi-color square with turtle
# import turtle

# def draw_multicolor_square(t, sz):
#     """Make turtle t draw a multi-color square of sz"""
#     for i in ['red', 'purple', 'hotpink', 'blue']:
#         t.color(i)
#         t.forward(sz)
#         t.left(90)

# wn = turtle.Screen()

# tess = turtle.Turtle()

# size = 20
# for i in range(15):
#     draw_multicolor_square(tess, size)
#     size += 10
#     tess.forward(10)
#     tess.right(15)

# wn.mainloop()


# # function can call other function
# def draw_rectangle(t, w, h):
#     """Get turtle t to draw a rectangle of width as w and height as h"""
#     for i in range(2):
#         t.forward(w)
#         t.left(90)
#         t.forward(h)
#         t.left(90)

# def draw_square(tx, sz):
#     draw_rectangle(tx, sz, sz)


# # compound interest calculate function
# def final_amt(p, r, n, t):
#     """
#     Apply the compound interest formula to p as capital, 
#     r as interest rate, n as compounding frequency, t as length of time
#     """
#     return p * (1 + r/n) ** (n*t)

# def final_amt_v2(principalAmount, nominalPercentageRate, numTimesPerYears, years):
#     return principalAmount * (1 + nominalPercentageRate/numTimesPerYears) ** (numTimesPerYears * years)

# def final_amt_v3(amt, rate, compounded, years):
#     return amt * (1 + rate/compounded) ** (compounded*years)

# toInvest = float(input('How much do you want to invest?'))
# fnl = final_amt(toInvest, 0.08, 12, 5)
# print("at the end of the period you'll have", fnl)


# Refactoring turtle code
import turtle

def make_window(color = 'white', title = 'Turtle'):
    """
    Set up the window with the given background color and title.
    Returns the new object of window
    """
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color, size):
    """
    Set up a turtle with the given color and pensize.
    returns the new object of turtle
    """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t

wn = make_window('lightgreen', 'Tess and Alex dancing in the dark')
tess = make_turtle('hotpink', 2)
alex = make_turtle('black', 3)
dave = make_turtle('yellow', 3)
wn.mainloop()