import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("lightblue")

# Create the turtle object for drawing the square
square = turtle.Turtle()

# Loop through colors and draw each side of the square
for color in ["red", "yellow", "green", "purple"]:
    square.color(color)  # Change the turtle's color for each side
    square.forward(200)  # Move forward 200 units
    square.left(90)      # Turn left by 90 degrees to form a square

# Set a delay before closing the window
win.delay(100)
win.exitonclick()
