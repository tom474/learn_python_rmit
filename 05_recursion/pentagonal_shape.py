def iter_pen_num(n):
    """
    This iterative function calculates the sum of the pentagonal number sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    sum_num = 1  # note the different start value and range here
    for i in range(1, n):
        sum_num += i*5
    return sum_num


def recur_pen_num(n):
    """
    This recursive function calculates the sum of the pentagonal number sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    if n == 0:
        return 1
    else:
        return (n-1)*5 + recur_pen_num(n-1)


def main():
    n = int(input("Enter the level of the pentagonal shape: "))
    print("The total dots: ", recur_pen_num(n))


main()
