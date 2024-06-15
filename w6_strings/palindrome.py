def is_palindrome(n):
    """
    This function checks if a string is palindrome (read the same forward and backward)
    :param n: a string
    :return: True/False
    """
    reversed_string = n[::-1]
    if n.lower() == reversed_string.lower():  # don't forget to lower the case just in case
        return True
    else:
        return False


def main():
    n = input("Enter a string: ")
    if is_palindrome(n):
        print(n, "is a palindrome")
    else:
        print(n, "is not a palindrome")


main()
