def filter_dict(dictionary, criteria):
    """
    This function filter the students who have marks greater than 170.
    :param dictionary: a dictionary
    :param criteria: the user's criteria
    :return: a filtered dictionary
    """
    # new_dict = {}
    # for key in dictionary.keys():  # check all pairs of key-value in the dictionary
    #     if dictionary[key] > criteria:  # check if the value is greater than 170
    #         new_dict[key] = dictionary[key]  # append it to the new dictionary
    new_dict = {key for key in dictionary if dictionary[key] > criteria}
    return new_dict


def main():
    """Main program"""
    dictionary = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
    criteria = int(input("Enter the criteria: "))
    print("Marks greater than", str(criteria) + ":", filter_dict(dictionary, criteria))  # print the output


main()
