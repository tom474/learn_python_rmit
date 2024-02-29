def remove_letter(n, letter):
    """
    This function removes all occurrences of a given letter (regardless of upper/lower case difference) from a string
    :param n: the full string
    :param letter: parts of the string to be removed
    :return: the result string
    """
    new_string = ''
    for char in n:
        if char.lower() != letter.lower():  # or you can write if char != c.lower() and char != c.upper():
            new_string = new_string + char
        # no need for else, as we would do nothing
    return new_string


def main():
    n = input("Enter a string: ")
    letter = input("Enter a letter that you want to remove: ")
    print(remove_letter(n, letter))


main()
