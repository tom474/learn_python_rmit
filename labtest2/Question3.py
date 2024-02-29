# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 2 - Question 3
# Author: Tran Manh Cuong (s3974735)
# Created date: 17/12/2022
# Last modified date: 17/12/2022
def find_max(num):
    """
    This function find the maximum value in the input sequence
    :param num: a sequence of numbers
    :return: the maximum value
    """
    num_list = num.split(" ")  # convert a sequence into a list
    new_num_list = [float(n) for n in num_list]  # change elements' type from string to float
    return max(new_num_list)


def find_position(num, max_num):
    """
    This function finds all max number's positions in the list
    :param num: a sequence of number
    :param max_num: the max number
    :return: positions
    """
    position = []  # a list contains max_value's positions
    num_list = num.split(" ")
    for i in range(len(num_list)):  # finds positions
        if num_list[i] == str(max_num):
            position.append(str(i))
    return ", ".join(position)


def main():
    """Main program"""
    num = input("Enter a sequence of numbers: ")  # get input from user
    print("The maximum value is", find_max(num), "at position(s)", find_position(num, find_max(num)))  # print the output


main()
