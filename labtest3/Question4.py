# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 3 - Question 4
# Author: Tran Manh Cuong (s3974735)
# Created date: 14/01/2023
# Last modified date: 14/01/2023
class MyPoint(object):
    def __init__(self, x, y, z):  # initialize x, y , z
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):  # add function to calculate p3
        return MyPoint(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):  # str function to print the output
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"


def main():
    """Main program"""
    p1 = MyPoint(1, 2, 3)
    p2 = MyPoint(2, 3, 4)
    print(p1)
    print(p2)
    p3 = p1 + p2
    print(p3)


main()
