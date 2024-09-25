import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("lightblue")

# Create the turtle object for drawing the octagon
octagon = turtle.Turtle()

# Loop through colors and draw each side of the octagon
for color in ["red", "blue", "yellow", "orange", "green", "purple", "pink", "grey"]:
    octagon.color(color)     # Change the turtle's color
    octagon.forward(100)     # Move forward 100 units
    octagon.left(45)         # Turn left by 45 degrees to form an octagon

# Set a delay before closing the window
win.delay(100)
win.exitonclick()
