import turtle
win = turtle.Screen()
win.bgcolor("lightgreen")

clock = turtle.Turtle()
clock.color("blue")
clock.shape("turtle")

for i in range(0, 360, 30):
    clock1 = turtle.Turtle()
    clock1.color("blue")
    clock1.shape("turtle")
    clock1.left(i)
    clock1.up()
    clock1.forward(100)
    clock1.down()
    clock1.forward(30)
    clock1.up()
    clock1.forward(30)

win.delay(100)
win.exitonclick()
