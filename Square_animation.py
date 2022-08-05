#import turtle library
import turtle

# create a new screen
screen = turtle.Screen()

# 500 x 500 window
screen.setup(500,500)

# create a new  turtle
don = turtle.Turtle()

# make it move faster
don.speed(20)

# a function that draws one square
def draw_square() :
    for side in range(4) :
        don.forward(100)
        don.left(90)

# go off-screen on the left
don.penup()
don.goto(-350, 0)
don.pendown()

# now do this repeatedly, to animate
while True :
    don.clear()             # - clear all the turtle's previous drawings
    draw_square()           # - draw a square
    don.forward(10)         # - move forward a bit
