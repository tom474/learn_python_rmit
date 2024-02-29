def is_odd(num):
    """
    This function returns True if the parameter is an odd number and False if it is even.
    :param num: an integer number
    :return: True or False
    """
    if num % 2 == 1:  # if the number is odd, return True
        return True
    elif num % 2 == 0:  # if the number is even, return False
        return False


def main():
    """Main program"""
    num = int(input("Enter a integer number: "))  # get input from user
    if is_odd(num):
        print(num, "is an odd number")  # print the output
    else:
        print(num, "is an even number")


main()
