import turtle
win = turtle.Screen()
win.bgcolor("lightblue")
square = turtle.Turtle()
for i in ["red", "yellow", "green", "purple"]:
    square.color(i)
    square.forward(200)
    square.left(90)
win.delay(100)
win.exitonclick()
