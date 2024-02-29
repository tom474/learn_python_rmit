import os

mess = input("Input your message: ")  # get input from user
folder_name = input("Input your folder name: ")
file_name = input("Input your file name: ")

file_path = folder_name + "\\" + file_name  # create file path
os.makedirs(folder_name, exist_ok=True)  # create folder
mess = (mess + "\n") * 100  # generate 100 lines of the message
with open(file_path, "w") as file:  # open file to write
    file.write(mess)  # write or append the message
