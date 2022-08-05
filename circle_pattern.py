import turtle

dharmaraj_wn = turtle.Screen()
turtle.speed(2)

for i in range (30):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.circle(i)
turtle.exitonclick()
