def is_even(num):
    """
    This function returns True if the parameter is an even number and False if it is odd.
    :param num: an integer number
    :return: True or False
    """
    if num % 2 == 0:  # if the number is even, return True
        return True
    elif num % 2 == 1:  # if the number is odd, return False
        return False


def main():
    """Main program"""
    num = int(input("Enter a integer number: "))  # get input from user
    if is_even(num):
        print(num, "is an even number")  # print the output
    else:
        print(num, "is an odd number")


main()
