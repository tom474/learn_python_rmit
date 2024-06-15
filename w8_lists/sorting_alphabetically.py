def reorder_words(words):
    """
    This function reorders the words given in a string alphabetically
    :param words: input a string of unordered words
    :return: string of ordered words
    """
    word_list = words.strip().split(",")  # split the input into a list of words
    sorted_word_list = sorted(word_list)  # sort the list alphabetically
    new_string = ",".join(sorted_word_list)  # convert the sorted list yo a string
    return new_string


def main():
    """Main program"""
    words = input("Enter a sequence of word: ") # get input from users
    print(reorder_words(words))  # show the output


main()
