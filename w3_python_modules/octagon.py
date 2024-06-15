import turtle
win = turtle.Screen()
win.bgcolor("lightblue")
octagon = turtle.Turtle()
for i in ["red", "blue", "yellow", "orange", "green", "purple", "pink", "grey"]:
    octagon.color(i)
    octagon.forward(100)
    octagon.left(45)
win.delay(100)
win.exitonclick()
