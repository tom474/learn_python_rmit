def iter_collatz(n):
    """
    This iterative function finds the max of the collatz sequences
    :param n: a number (int)
    :return: max of the sequences
    """
    max_number = 0
    while True:
        if max_number < n:
            max_number = n
        if n == 1:
            break
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
    return max_number


# Version 1: passing max_num as a parameter
def recur_collatz1(n, max_number):
    """
    This recursive function finds the max of the collatz sequences
    :param n: a number (int)
    :param max_number:
    :return: max of the sequences
    """
    if max_number < n:
        max_number = n
    if n == 1:
        return max_number
    else:
        print(n)
        if n % 2 == 0:
            return recur_collatz1(n / 2, max_number)
        else:
            return recur_collatz1(n * 3 + 1, max_number)


# Version 2: using max() function
def recur_collatz2(n):
    """
    This iterative function finds the max of the collatz sequences
    :param n: a number (int)
    :return: max of the sequences
    """
    if n == 1:
        return 1
    else:
        print(n)
        if n % 2 == 0:
            return max(n, recur_collatz2(n/2))
        else:
            return max(n, recur_collatz2(n*3+1))


# Version 3: only 1 call of the function
def recur_collatz3(n):
    """
    This iterative function finds the max of the collatz sequences
    :param n: a number (int)
    :return: max of the sequences
    """
    if n == 1:
        return 1
    else:
        print(n)
        if n % 2 == 0:
            i = n/2
            return max(n, recur_collatz3(i))
        else:
            i = n*3+1
            return max(n, recur_collatz3(i))


def main():
    n = int(input("Enter a number: "))
    max_number = 0
    print("Max collatz:", recur_collatz1(n, max_number))


main()
