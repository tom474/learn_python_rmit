import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("lightblue")

# Create the turtle object for drawing the hexagon
hexagon = turtle.Turtle()

# Loop through colors and draw each side of the hexagon
for color in ["red", "blue", "yellow", "orange", "green", "purple"]:
    hexagon.color(color)     # Change the turtle's color
    hexagon.forward(100)     # Move forward 100 units
    hexagon.left(60)         # Turn left by 60 degrees to form a hexagon

# Set a delay before closing the window
win.delay(100)
win.exitonclick()
