import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("lightblue")

# Create the turtle object for drawing the equilateral triangle
equilateral_triangle = turtle.Turtle()

# Loop through colors and draw each side of the triangle
for color in ["red", "green", "yellow"]:
    equilateral_triangle.color(color)
    equilateral_triangle.forward(200)  # Move forward 200 units
    equilateral_triangle.left(120)     # Turn left by 120 degrees to form an equilateral triangle

# Set a delay before closing the window
win.delay(100)
win.exitonclick()
