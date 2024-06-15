def append_message(mes):
    """
    This function append the message 100 times into a file named message.txt
    :param mes: user's message
    :return: message.txt
    """
    with open("messages.txt", "a") as file:
        for i in range(100):
            file.write(mes + "\n")


def main():
    """Main program"""
    mes = input("Enter a message: ")  # get input from user
    append_message(mes)


main()
