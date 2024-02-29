def count_letters(string):
    """
    This function creates a dictionary from a string, key is the letter and value is the count of the letters
    :param string: a string
    :return: a dictionary showing the letter frequencies
    """
    letter_dict = {}  # create an empty dictionary
    for letter in string:  # count letter in the string
        letter_dict[letter] = string.count(letter)  # key is the letter, value is the count of that letter
    return letter_dict


def main():
    """Main program"""
    string = input("Enter a string: ")  # get input from user
    print(count_letters(string))  # print the output


main()
