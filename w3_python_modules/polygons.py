import turtle
win = turtle.Screen()
win.bgcolor("lightblue")
polygon = turtle.Turtle()


def check_side(n):
    if n == 3:
        for i in ["red", "green", "yellow"]:
            polygon.color(i)
            polygon.forward(200)
            polygon.left(120)
    elif n == 4:
        for i in ["red", "yellow", "green", "purple"]:
            polygon.color(i)
            polygon.forward(200)
            polygon.left(90)
    elif n == 6:
        for i in ["red", "blue", "yellow", "orange", "green", "purple"]:
            polygon.color(i)
            polygon.forward(100)
            polygon.left(60)
    elif n == 8:
        for i in ["red", "blue", "yellow", "orange", "green", "purple", "pink", "grey"]:
            polygon.color(i)
            polygon.forward(100)
            polygon.left(45)


def main():
    n = int(input("Enter the number of sides you want: "))
    check_side(n)


main()
win.delay(100)
win.exitonclick()
