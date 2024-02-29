# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 1 - Question 4
# Author: Tran Manh Cuong (s3974735)
# Created date: 19/11/2022
# Last modified date: 19/11/2022
def reverse_number(num):
    """
    function reverses a given integer number
    :param num: an integer
    :return: reversed number
    """
    rev_num = 0
    while num != 0:
        rev_num = (rev_num * 10) + (num % 10)
        num //= 10
    return rev_num


def main():
    """Main program"""
    num = int(input("Enter an integer: "))  # get user's input
    if num < 0:  # negative number situation
        neg = -num
        print("The reversed number is: -" + str(reverse_number(neg)))
    else:   # positive number situation
        print("The reversed number is:", reverse_number(num))


main()
