def iter_harmonic(n):
    """
    This iterative function calculates the sum of the harmonic sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    sum_num = 0
    for i in range(1, n+1):
        sum_num += 1/i
    return sum_num


def recur_harmonic(n):
    """
    This recursive function calculates the sum of the harmonic sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    if n == 1:
        return 1
    else:
        return 1/n + recur_harmonic(n-1)


def main():
    n = int(input("Enter a positive integer: "))
    print(recur_harmonic(n))


main()
