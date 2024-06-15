# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 2 - Question 2
# Author: Tran Manh Cuong (s3974735)
# Created date: 17/12/2022
# Last modified date: 17/12/2022
def string_to_list(string):
    """
    This function converts a string to a list
    :param string: a string
    :return: a list
    """
    word_list = string.split(",")  # convert a string into a list
    return word_list


def non_vowel(word_list):
    """
    This function filters the words that do not start with vowel alphabets
    :param word_list: a list
    :return: filtered words in separate lines
    """
    vowels = "aeiou"
    for word in word_list:  # check which words in the list is not start with a vowel
        if word.lower()[0] not in vowels:
            print(word)


def main():
    """Main program"""
    string = input("Enter the words seperated by comma: ")  # get input from user
    print(string_to_list(string))  # print the words list
    non_vowel(string_to_list(string))  # print words not start with a vowel


main()
