import os


# Functions
def write_code(folder_name, file_name, code):
    """
    This function writes the source code for drawing a circle using Turtle to a file
    :param folder_name: the folder name input by user
    :param file_name: the file name input by user
    :param code: the source code for drawing a circle
    :return: a file has source code
    """
    file_path = folder_name + "\\" + file_name
    os.makedirs(folder_name, exist_ok=True)
    with open(file_path, "w") as file:
        file.write(code)


def main():
    folder_name = input("Enter the folder name: ")  # get input from user
    file_name = input("Enter the file name: ")
    code = """# import section
import turtle

win = turtle.Screen()  # set up a screen
win = turtle.bgcolor("red")  # set the back ground color
t = turtle.Turtle()  # initializing the turtle

r = 50  # radius of the circle
t.circle(50)  # draw a circle
win.exitonclick  # close the canvas window with a click
    """
    write_code(folder_name, file_name, code)


main()