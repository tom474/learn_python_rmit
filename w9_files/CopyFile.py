def copy_file(in_file_path):
    """
    This function copies all lines from the file that exist before and insert a number into each line to a new file
    :param in_file_path: existing file
    :return: new file
    """
    # convert to list, alter the filename, the join str to out_file_path
    line_list = in_file_path.split("\\")  # split the directory
    line_list[-1] = 'new_' + line_list[-1]  # rename the old file to new file
    out_file_path = "\\".join(line_list)  # make directory

    with open(out_file_path, "w") as out_file:  # open out_file_path to write/append
        with open(in_file_path, "r") as in_file:  # open in_file_path to read
            lines = in_file.readlines()  # read all lines into a list
            number = 1
            for line in lines:  # loop through the list
                new_line = str(number) + "\t" + line  # append numbers and write to new file
                number += 1
                out_file.write(new_line)  # write to the new file


def main():
    in_file_path = "teacher\\messages.txt"
    copy_file(in_file_path)


main()
