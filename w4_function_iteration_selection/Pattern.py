# def recursive(n):
#     """
#     This function will print numbers by pattern.
#     :param n: input integer
#     :return: all the integers from the list which from the desginated pattern
#     """
#     num = [i + 1 for i in range(n)]
#     if n == 1:
#         return 1
#     print(" ".join(map(str, num)))
#     return recursive(n - 1)
#
# print(recursive(5))


# def number_pattern(n):
#     """
#     This is a non-fruitful function to print out pattern
#     :param n: a number (int)
#     :return: None
#     """
#     # for j in range(n):
#     while n > 0:
#         for i in range(1, n+1):
#             print(i, end=' ')
#         print()
#         n -= 1
#
# number_pattern(5)


def number_pattern(n):
    """
    This is a non-fruitful function to print out pattern 1 line
    :param n: a number (int)
    :return: None
    """
    for i in range(1, n + 1):
        print(i, end=' ')


def mul_line_pattern(n):
    """
    This is a non-fruitful function to print out pattern multiple lines
    :param n: a number (int)
    :return: None
    """
    for j in range(n, 0, -1):
        number_pattern(j)
        print()


mul_line_pattern(5)
