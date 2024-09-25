def eng_to_pirate_dict(dict_path):
    """
    This function creates a dictionary from a text file
    :param dict_path: the file containing the dictionary
    :return: a Python dictionary
    """
    with open(dict_path, "r") as file:  # open the file
        lines = file.readlines()  # read each line in the text
        pirate_dict = {}  # create an empty dictionary
        for line in lines:
            line = line.replace("\n", "")  # combine all lines to one lines
            line = line.split("\t")  # convert the string into list
            eng_word = line[0].strip().lower()  # the first element is the key
            pirate_word = line[-1].strip().lower()  # the second one is value
            pirate_dict[eng_word] = pirate_word  # append the key-value pair to the dictionary
    return pirate_dict


def eng_to_pirate(dict_path, sen):
    """
    This function translate an English sentence to a pirate one
    :param dict_path: the file path containing the dictionary
    :param sen: the sentence to translate
    :return: sentence in pirate
    """
    pirate_dict = eng_to_pirate_dict(dict_path)  # call the dictionary from the previous function
    word_list = sen.split(" ")  # convert the sentence into a list
    pirate_word_list = []  # create an empty list
    for word in word_list:
        if word.strip().lower() in pirate_dict:
            pirate_word_list.append(pirate_dict[word.strip().lower()])  # convert english words into pirate
        else:
            pirate_word_list.append(word.strip().lower())  # if it not in the dictionary, print the english word
    pirate_sen = " ".join(pirate_word_list).capitalize()  # make a sentence
    return pirate_sen


def main():
    """Main program"""
    string = input("Enter a english sentence: ")  # get input from user
    print(eng_to_pirate("english_to_pirate.txt", string))  # print the output


main()
