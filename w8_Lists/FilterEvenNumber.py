def filter_even(num):
    """
    This function filter even number in a list
    :param num: the max number of the list
    :return: a list of even numbers
    """
    even_num_list = [i for i in range(num+1) if i % 2 == 0]  # generate a list contains even number
    return even_num_list


def main():
    """Main program"""
    num = int(input("Enter a number: "))  # get input from users
    print(filter_even(num))  # print the result


main()
