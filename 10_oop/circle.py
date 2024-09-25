import math


class Circle(object):
    def __init__(self, radius):  # constructor
        self.radius = radius

    def set_radius(self):
        return self.radius

    def get_radius(self, radius):
        self.radius = radius

    def get_area(self):  # get area of a circle
        return math.pi*self.radius**2

    def get_perimeter(self):  # get the perimeter of a circle
        return 2*math.pi*self.radius


def main():
    """Main program"""
    circle = Circle(11)
    print(circle.get_area())
    circle = Circle(4.44)
    print(circle.get_perimeter())


main()
