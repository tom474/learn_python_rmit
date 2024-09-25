def table(num):
    """
    This function creates a neatly formatted multiplication table
    :param num: an integer number
    :return: a neatly formatted multiplication table
    """
    print("x", end="\t")  # print letter "x"
    for i in range(num):  # print the first row
        print(i, end="\t")
    print(num)
    for j in range(num+1):  # print second row
        print(j, end="\t")
        for k in range(num+1):  # print column
            print(j*k, end="\t")
        print("")


def main():
    """Main program"""
    num = int(input("Enter an integer number: "))  # get input from user
    table(num)


main()
