import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("lightblue")

# Create the turtle object for drawing the polygon
polygon = turtle.Turtle()


def check_side(n):
    if n == 3:  # Triangle
        for color in ["red", "green", "yellow"]:
            polygon.color(color)
            polygon.forward(200)
            polygon.left(120)
    elif n == 4:  # Square
        for color in ["red", "yellow", "green", "purple"]:
            polygon.color(color)
            polygon.forward(200)
            polygon.left(90)
    elif n == 6:  # Hexagon
        for color in ["red", "blue", "yellow", "orange", "green", "purple"]:
            polygon.color(color)
            polygon.forward(100)
            polygon.left(60)
    elif n == 8:  # Octagon
        for color in ["red", "blue", "yellow", "orange", "green", "purple", "pink", "grey"]:
            polygon.color(color)
            polygon.forward(100)
            polygon.left(45)
    else:
        print("This shape is not supported.")


def main():
    n = int(input("Enter the number of sides you want (3, 4, 6, 8): "))
    check_side(n)


main()

# Set a delay before closing the window
win.delay(100)
win.exitonclick()
