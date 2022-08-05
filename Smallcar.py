
# Import required library
import turtle


samllcar = turtle.Turtle()


# Below code for drawing rectangular upper body
samllcar.color('#008000')
samllcar.fillcolor('#008000')
samllcar.penup()
samllcar.goto(0,0)
samllcar.pendown()
samllcar.begin_fill()
samllcar.forward(370)
samllcar.left(90)
samllcar.forward(50)
samllcar.left(90)
samllcar.forward(370)
samllcar.left(90)
samllcar.forward(50)
samllcar.end_fill()


# Below code for drawing window and roof
samllcar.penup()
samllcar.goto(100, 50)
samllcar.pendown()
samllcar.setheading(45)
samllcar.forward(70)
samllcar.setheading(0)
samllcar.forward(100)
samllcar.setheading(-45)
samllcar.forward(70)
samllcar.setheading(90)
samllcar.penup()
samllcar.goto(200, 50)
samllcar.pendown()
samllcar.forward(49.50)


# Below code for drawing two tyres
samllcar.penup()
samllcar.goto(100, -10)
samllcar.pendown()
samllcar.color('#000000')
samllcar.fillcolor('#000000')
samllcar.begin_fill()
samllcar.circle(20)
samllcar.end_fill()
samllcar.penup()
samllcar.goto(300, -10)
samllcar.pendown()
samllcar.color('#000000')
samllcar.fillcolor('#000000')
samllcar.begin_fill()
samllcar.circle(20)
samllcar.end_fill()


samllcar.hideturtle()

