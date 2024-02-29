# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 3 - Question 2
# Author: Tran Manh Cuong (s3974735)
# Created date: 14/01/2023
# Last modified date: 14/01/2023
def remove_item(dictionary):
    """
    This function removes all items that have "DELETE" value
    :param dictionary: a given dictionary
    :return: new dictionary
    """
    new_dictionary = {key: value for key, value in dictionary.items() if value != 'DELETED'}  # remove items that have "DELETE" value
    return new_dictionary


def write_to_txt(new_dict):
    """
    This function writes the result to file output.txt
    :param new_dict: a dictionary
    :return: output.txt
    """
    with open("output.txt", "w") as file:  # write the dictionary to output.txt
        for key, value in new_dict.items():
            file.write(f"{key}: {value}\n")


def main():
    """Main program"""
    student = {
        'ID': 's3974735',
        'Name': 'Cuong Tran',
        'University': 'RMIT',
        'Major': 'Information Technology',
        'Year': 2022,
        'Python': 'DI',
        'OOP': 'HD',
        'Network': 'DELETED',
        'C++': 'DI',
        'Web': 'DELETED',
        'Java': 'CR'
    }
    write_to_txt(remove_item(student))


main()
