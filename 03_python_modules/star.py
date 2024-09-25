import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("lightblue")

# Create the turtle object for drawing the star
star = turtle.Turtle()

# Loop to draw a 5-pointed star
for i in range(5):
    star.forward(200)  # Move forward 200 units
    star.right(144)    # Turn right by 144 degrees to create the star shape

# Set a delay before closing the window
win.delay(100)
win.exitonclick()
