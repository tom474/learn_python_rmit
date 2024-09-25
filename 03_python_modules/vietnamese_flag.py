import turtle

# Set up the screen with a red background
win = turtle.Screen()
win.bgcolor("red")

# Create the turtle object for drawing the star
vn = turtle.Turtle()
vn.color("yellow")  # Set the turtle's outline color to yellow
vn.fillcolor("yellow")  # Set the fill color to yellow

# Move the turtle to the starting position
vn.up()
vn.goto(-100, 0)  # Position the turtle at (-100, 0)
vn.down()

# Start filling the star
vn.begin_fill()

# Draw a 5-pointed star
for i in range(5):
    vn.forward(200)
    vn.right(144)

# End filling the star
vn.end_fill()

# Set a delay before closing the window
win.delay(100)
win.exitonclick()
