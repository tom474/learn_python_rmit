def find_max(dictionary):
    """
    This function finds the max key's value in the dictionary
    :param dictionary: a dictionary
    :return: the max number
    """
    value_list = [dictionary[key] for key in dictionary]
    return max(value_list)


def find_max_key(dictionary, max_value):
    """
    This function finds all the key which have the max value
    :param dictionary: a dictionary
    :param max_value: the max value in the dictionary
    :return: max key
    """
    max_key_list = [key for key in dictionary if dictionary[key] == max_value]
    return ",".join(max_key_list)


def main():
    """Main program"""
    dictionary = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
    print("The maximum value in the dictionary is", find_max(dictionary), "of the key", find_max_key(dictionary, find_max(dictionary)))


main()
