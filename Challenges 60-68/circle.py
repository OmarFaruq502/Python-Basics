#----------------------------------------------
#       Problem 060
#       Author: Omar Rahman
#       Date: 1/1/2019
#----------------------------------------------

#--------------
# Circle
#--------------
import turtle

turtle.shape("turtle")

Screen = turtle.Screen()
Screen.bgcolor("green")

turtle.pensize(3)

turtle.color("red","red")
turtle.begin_fill()

#----------------------
for i in range(0,360):
    turtle.forward(1)
    turtle.right(1)
#----------------------

turtle.end_fill()
turtle.exitonclick()