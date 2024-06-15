# Exercise 2: Area of a circle
import math  # import the math module
pi_number = math.pi  # assign the value of pi number from math module to a variable
radius = float(input('Enter radius: '))  # get the radius from user input and convert it from str to float
circle_area = pi_number*(radius**2)  # calculation
print("Area of the circle is", circle_area)  # no str() and empty space needed when using ","
