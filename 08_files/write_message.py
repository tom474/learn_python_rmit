def write_messages(message):
    """
    This function writes the user's message 100 times in a file named messages.txt
    :param message: user's message
    :return: 100 times of the message in messages.txt
    """
    with open("messages.txt", "w") as file:
        for i in range(100):  # write the user's message 100 times in the file
            file.write(message + "\n")


def main():
    """Main program"""
    message = input("Enter the message: ")  # get input from users
    write_messages(message)  # run the function


main()
