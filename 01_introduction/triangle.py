# Define global variables
x = 2
y = 2
z = 3


def triangle_type(a, b, c):
    """
    Determines the type of triangle based on its sides.

    :param a: First side of the triangle
    :param b: Second side of the triangle
    :param c: Third side of the triangle
    :return: The sum of all sides
    """
    # Check if the triangle is equilateral
    if a == b == c:
        print("Equilateral")

    # Check if the triangle is isosceles
    # Use elif and != to ensure exclusive conditions
    elif a == b != c or b == c != a or a == c != b:
        print("Isosceles")

    # Check if the triangle is scalene
    else:
        print("Scalene")

    # Calculate and return the sum of all sides
    return a + b + c


# Try-except block for error handling
try:
    # Check if the sides form a valid triangle
    if x + y > z and y + z > x and x + z > y:
        print("It's a triangle")

        # Call the function to check triangle type and calculate the sum of sides
        sum_sides = triangle_type(x, y, z)
        print(f"Sum of the sides is: {sum_sides}")
    else:
        print("Not a triangle")
except Exception as e:
    print(f"Error: {e}")
