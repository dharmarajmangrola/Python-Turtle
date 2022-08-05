# import turtle library

import turtle
             
dharmaraj_wn = turtle.Screen()
dharmaraj_wn.bgcolor("light blue")
dharmaraj_wn.title("Turtle")
dharmaraj_pen = turtle.Turtle()
dharmaraj_pen.color("black")
turtle.speed(1)
def dharmaraj_sqrfunc(size):
   for i in range(4):
      dharmaraj_pen.fd(size)
      dharmaraj_pen.left(90)
      size = size - 5
dharmaraj_sqrfunc(146)
dharmaraj_sqrfunc(126)
dharmaraj_sqrfunc(106)
dharmaraj_sqrfunc(86)
dharmaraj_sqrfunc(66)
dharmaraj_sqrfunc(46)
dharmaraj_sqrfunc(26)
