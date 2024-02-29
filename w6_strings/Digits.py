def count_digit(n):
    """
    This function counts the number of digits of an integer and return that number, positive integer
    :param n: an integer
    :return: digit count
    """
    return len(str(abs(n)))


def main():
    n = int(input("Enter a integer number: "))
    print(n, "have", count_digit(n), "digits")


main()
