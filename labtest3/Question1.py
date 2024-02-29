# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 3 - Question 1
# Author: Tran Manh Cuong (s3974735)
# Created date: 14/01/2023
# Last modified date: 14/01/2023
def remove_number(string):
    """
    This function removes numbers of a given string
    :param string: given string
    :return: a list of words
    """
    word_list = string.split()  # convert string into list
    new_list = []  # create a new list
    for word in word_list:
        if word.isdigit():  # check if string has digits and remove digits
            continue
        else:
            for i in word:  # check every letter if it is a number
                if i.isdigit():
                    break
                else:
                    if word not in new_list:
                        new_list.append(word)  # append to new list if it not contains number
    return new_list


def reverse_string(word_list):
    """
    This function reverse the order of the filtered string
    :param word_list: list of words
    :return: reverse string
    """
    reverse_list = []
    for i in range(len(word_list)-1, -1, -1):  # for loop to reverse the list
        reverse_list.append(word_list[i])
    return " ".join(reverse_list)  # convert list into string


def main():
    """Main program"""
    string = input("Enter a string with words and numbers: ")  # get input from user
    print(reverse_string(remove_number(string)))  # print the output


main()
