import turtle
win = turtle.Screen()
win.bgcolor("lightblue")
equilateral_triangle = turtle.Turtle()
for i in ["red", "green", "yellow"]:
    equilateral_triangle.color(i)
    equilateral_triangle.forward(200)
    equilateral_triangle.left(120)
win.delay(100)
win.exitonclick()
