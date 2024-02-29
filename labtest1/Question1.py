# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 1 - Question 1
# Author: Tran Manh Cuong (s3974735)
# Created date: 19/11/2022
# Last modified date: 19/11/2022
def print_number(num):
    """
    This function prints all integers in the interval [n, 4n) that are divisible by 7
    :param num: an integer
    :return: all integers in the interval [n, 4n) that are divisible by 7
    """
    for i in range(num, 4 * num, 1):  # A loop to check all integers in the interval [n, 4n)
        if i % 7 == 0:  # Checking if the number is divisible by 7
            print(i)


def main():
    """Main program"""
    while True:  # If the input number is not greater than 2, user need to input it again
        num = int(input("Enter an integer number: "))  # Get user's input
        if num > 2:
            break
        else:
            continue
    print_number(num)


main()
