# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 2 - Question 1
# Author: Tran Manh Cuong (s3974735)
# Created date: 17/12/2022
# Last modified date: 17/12/2022
import string


def count_letters(s):
    """
    This function counts letters in a string
    :param s: a string
    :return: number of letters
    """
    count = 0
    for i in s.lower():  # count how many letters in the string
        if i in string.ascii_lowercase:
            count += 1
    return count


def count_digits(s):
    """
    This function counts digits in a string
    :param s: a string
    :return: number of digits
    """
    count = 0
    for i in s.lower():  # count how many digits in the string
        if i in string.digits:
            count += 1
    return count


def count_symbols(s):
    """
    This function counts symbols in a string
    :param s: a string
    :return: number of symbols
    """
    count = 0
    for i in s.lower():  # count how many symbols in the string
        if i in string.punctuation or i == " ":
            count += 1
    return count


def main():
    """Main program"""
    s = input("Enter a string: ")  # get input from user
    print("Letter:", count_letters(s))  # print the output
    print("Digits:", count_digits(s))
    print("Symbols:", count_symbols(s))


main()
