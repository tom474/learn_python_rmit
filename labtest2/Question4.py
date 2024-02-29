# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 2 - Question 4
# Author: Tran Manh Cuong (s3974735)
# Created date: 17/12/2022
# Last modified date: 17/12/2022
def representative_board(num):
    """
    This function computes the number of possible ways to select a representative board from n students.
    :param num: the number of student
    :return: number of way(s) to select a representative board
    """
    if num == 1:
        return 1
    return num + representative_board(num-1)


def main():
    """Main program"""
    num = int(input("Enter the number of students: "))  # get input from user
    print("There are", 1 + representative_board(num), "way(s) to select a representative board from", num, "student(s)")


main()
