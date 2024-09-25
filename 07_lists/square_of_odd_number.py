def square_of_odd(num):
    """
    This function generates a sequence of comma-separated squares of odd numbers
    :param num: a list of numbers as a string
    :return: a sequence of comma-separated squares of odd numbers
    """
    num_list = num.strip().split(",")  # generate a list contains seperated numbers
    odd_num_list = [str(int(i) ** 2) for i in num_list if int(i) % 2 == 1]  # generate a list of squares of odd numbers
    sequence = ",".join(odd_num_list)  # convert elements from the list into a sequence
    return sequence


def main():
    """Main program"""
    num = input("Enter a list of numbers: ")  # get input from users
    print(square_of_odd(num))  # print the output


main()
