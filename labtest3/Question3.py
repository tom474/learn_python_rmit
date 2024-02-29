# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 3 - Question 3
# Author: Tran Manh Cuong (s3974735)
# Created date: 14/01/2023
# Last modified date: 14/01/2023
def cal_invest(data_file_name):
    """
    This function calculates the total investment
    :param data_file_name:
    :return: total investment
    """
    total_invest = 0
    with open(data_file_name, "r") as file:  # read the file
        for line in file:  # calculate the total investment
            stock_data = line.strip().split(',')  # convert string into list
            shares = int(stock_data[1])
            value = float(stock_data[2])
            total_invest += shares * value
    return total_invest


def main():
    """Main program"""
    in_data_file_name = input("Input the data file's name: ")  # get input from user
    investment_amount = cal_invest(in_data_file_name)  # calculate total investment
    print(f"Total investment amount in {in_data_file_name}: {investment_amount}")  # print the output


main()


