#----------------------------------------------
#       Testing Turtle
#----------------------------------------------
import turtle
turtle.shape("turtle")

Screen = turtle.Screen()

Screen.bgcolor("yellow")

turtle.pensize(3)

turtle.color("black","red")
turtle.begin_fill()

for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(100)
        turtle.right(72)

turtle.end_fill()
turtle.exitonclick()