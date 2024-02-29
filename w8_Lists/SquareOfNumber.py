def square_of_number(num):
    """
    This function generates the list of squares of positive integers for 1 to n (inclusively)
    :param num: an integer
    :return: list of square numbers
    """
    num_list = [i ** 2 for i in range(1, num+1)]  # a list with all square of numbers
    return num_list


def main():
    """Main program"""
    num = int(input("Enter a number: "))  # get user input
    print(square_of_number(num)[-5:])  # print the last 5 elements of the list


main()
