import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("lightgreen")

# Main turtle for the clock
clock = turtle.Turtle()
clock.color("blue")
clock.shape("turtle")

# Loop to draw the hour markers for the clock
for i in range(0, 360, 30):  # 360 degrees, 12 markers, so 30 degrees apart
    clock_marker = turtle.Turtle()
    clock_marker.color("blue")
    clock_marker.shape("turtle")

    clock_marker.left(i)  # Turn the turtle to the correct angle
    clock_marker.up()  # Lift pen to move without drawing
    clock_marker.forward(100)  # Move to the correct position
    clock_marker.down()  # Start drawing
    clock_marker.forward(30)  # Draw the hour marker
    clock_marker.up()  # Lift pen again
    clock_marker.forward(30)  # Move slightly forward to simulate space

# Set a delay before the window closes
win.delay(100)
win.exitonclick()
