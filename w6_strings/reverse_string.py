def reverse_string(n):
    """
    This function returns the reverse of its string parameter
    :param n: a string
    :return: a reverse string
    """
    return n[::-1]


def main():
    n = input("Enter a string: ")
    print(reverse_string(n))


main()
