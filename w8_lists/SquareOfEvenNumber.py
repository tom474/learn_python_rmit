def square_of_even(num):
    """
    This function generates a list contains square of even number
    :param num: the maximum number
    :return: a list contains square of even number
    """
    num_list = [i ** 2 for i in range(num+1) if i % 2 == 0]  # generate a list contains square of even number
    return num_list


def main():
    """Main program"""
    num = int(input("Enter a number: "))  # get user input
    print(square_of_even(num))  # print a list contains square of even numbers


main()
