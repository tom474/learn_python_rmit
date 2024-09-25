def iter_tri_num(n):
    """
    This iterative function calculates the sum of the triangular number sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    sum_num = 0
    for i in range(1, n+1):
        sum_num += i
        print(sum_num)
    return sum_num


def recur_tri_num(n):
    """
    This recursive function calculates the sum of the triangular number sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    if n == 1:
        return 1
    else:
        return n + recur_tri_num(n-1)


# another version if you want to print
def recur_tri_num2(n):
    """
    This recursive function calculates the sum of the triangular number sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    if n == 1:
        return 1
    else:
        i = recur_tri_num2(n-1)
        print(i)
        return n + i


def main():
    n = int(input("Enter a number: "))
    print(recur_tri_num(n))


main()
