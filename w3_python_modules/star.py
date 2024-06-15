import turtle
win = turtle.Screen()
win.bgcolor("lightblue")
star = turtle.Turtle()
for i in range(5):
    star.forward(200)
    star.right(144)
win.delay(100)
win.exitonclick()
