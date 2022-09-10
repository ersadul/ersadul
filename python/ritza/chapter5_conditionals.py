# # 5.5. Conditional execution
# x = int(input('x?'))
# if x % 2 == 0:
#     print(x, 'is even.')
# else:
#     print(x, 'is odd.')

# 5.12. A Turtle Bar Chart
import turtle

def draw_bar(t, height):
    """Get turtle t to draw one bar, of height. """
    t.left(90)
    t.forward(height)
    t.right(90)
    t.write('  '+str(height) )
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.forward(10)
    
wn = turtle.Screen()
alex = turtle.Turtle()
alex.begin_fill() #begin to fill the turtle object
alex.color('black','pink')


xs = [48, 117, 200, 240, 160, 260, 220]

for v in xs:
    draw_bar(alex, v)

alex.end_fill()

wn.mainloop()