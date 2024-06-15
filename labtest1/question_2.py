# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 1 - Question 2
# Author: Tran Manh Cuong (s3974735)
# Created date: 19/11/2022
# Last modified date: 19/11/2022
def factorial(num):
    """
    A function to find the factorial of a positive integer number
    :param num: an integer
    :return: the factorial of a positive integer number
    """
    factorial_num = 1
    if num == 0:  # The factorial of 0 is 1
        factorial_num = 1
    else:
        for i in range(1, num + 1, 1):  # calculating the factorial number
            factorial_num = factorial_num * i
    return factorial_num


def main():
    """Main program"""
    num = int(input("Enter an integer number: "))  # get user's input
    if num >= 0:  # there is no factorial for negative numbers
        print("The factorial of", num, "is:", factorial(num))
    else:
        print("Factorial does not exist for negative numbers")


main()
