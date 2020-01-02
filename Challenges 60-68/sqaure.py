#----------------------------------------------
#       Problem 060
#       Author: Omar Rahman
#       Date: 1/1/2019
#----------------------------------------------

import turtle

turtle.shape("turtle")

Screen = turtle.Screen()
Screen.bgcolor("yellow")

turtle.pensize(3)

turtle.color("green","red")
turtle.begin_fill()

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.end_fill()
turtle.exitonclick()