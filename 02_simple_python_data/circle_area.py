# Exercise 2: Area of a circle

# Import the math module for mathematical operations
import math

# Assign the value of pi from the math module to a variable
pi_number = math.pi

# Get the radius from user input and convert it to float
radius = float(input("Enter radius: "))

# Calculate the area of the circle
circle_area = pi_number * (radius ** 2)

# Output the area of the circle
print("Area of the circle is", circle_area)
