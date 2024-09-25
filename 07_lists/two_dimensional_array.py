def generate_array(num):
    """
    This function generates a 2-dimensional array (multiplication table).
    :param num: X,Y - 2 digits as input
    :return: 2-dimensional array
    """
    dimensions = [int(x) for x in num.split(",")]  # append X and Y to the list
    row = dimensions[0]  # row is X
    col = dimensions[1]  # col is Y
    large_list = []  # start with empty big list
    for r in range(row):  # for each row
        small_list = []
        for c in range(col):  # complete every row
            small_list.append(r*c)
        large_list.append(small_list)
    return large_list


def main():
    """Main program"""
    num = input("Enter X,Y: ")  # get user input
    for i in range(len(generate_array(num))):
        print(generate_array(num)[i])  # print the return value of the function


main()
