import turtle
win = turtle.Screen()
win.bgcolor("lightblue")
hexagon = turtle.Turtle()
for i in ["red", "blue", "yellow", "orange", "green", "purple"]:
    hexagon.color(i)
    hexagon.forward(100)
    hexagon.left(60)
win.delay(100)
win.exitonclick()
