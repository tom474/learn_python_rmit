def remove_str(s, substr):
    """
    This function removes all occurrences of a substring in a string
    :param s: original string
    :param substr: substring to be removed
    :return: result string
    """
    new_str = ""
    len_str_1 = len(substr)
    len_str_2 = len(s)
    index = 0
    while index != len_str_2:
        if substr == s[index:(index+len_str_1)]:
            index += len_str_1
            continue
        else:
            new_str += s[index]
            index += 1
    return new_str


def main():
    s = input("Enter a string: ")
    substring = input("Enter a string that you want to remove: ")
    print(remove_str(s, substring))


main()
