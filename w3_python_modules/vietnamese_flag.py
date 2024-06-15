import turtle
win = turtle.Screen()
win.bgcolor("red")
vn = turtle.Turtle()
vn.color("yellow")
vn.up()
vn.goto(-100, 0)
vn.down()
vn.fillcolor()
vn.begin_fill()
for i in range(5):
    vn.forward(200)
    vn.right(144)
vn.end_fill()

win.delay(100)
win.exitonclick()
