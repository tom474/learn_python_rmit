# Challenge exercise: The Collatz Sequence
# Yes, there is a name for this sequence, and also a conjecture https://en.wikipedia.org/wiki/Collatz_conjecture

# define variables to count the max
max_step = 0
max_step_N = 0
max_N = 0
max_N_seq = 0

# This is for question 3 where ori_N == count
equal_list = []  # to define an empty list, just use square bracket with nothing in it

# the main for loop
for N in range(1, 101, 1):  # range(start,stop,step), note that stop is not inclusive, so we have to use 101
    ori_N = N  # temporarily store the starting N of each sequence
    count = 0  # set the count of steps for each sequence

    # !Important! use for loop while dev and test first: for i in range(1000000):
    while True:
        # put print function here if you want to print N for each sequence
        # print(N)

        # this if block is to get the max possible N in all sequences
        if N > max_N:
            max_N = N
            max_N_seq = ori_N

        # this if block is the stopping condition of the while loop
        if N == 1:
            break  # note: break here will only break out of the while loop, not the outer for loop

        # this if/else block is the main rules of the sequence
        if N % 2 == 0:
            N = N/2
        else:
            N = N*3 + 1  # remember what will happen if we change this to:    N = N*3 - 1
        # this is the count for the number of steps for each sequence
        # other way to write it:    count = count + 1
        count += 1

    # pay an attention to indentation, they will change the logic of your code

    # this if block is to find when number of steps = number of starting N of that sequence
    # !!! You can try out the unequal condition if count != ori_N:
    # in case you only want to print it out:
    # if count == ori_N:
    #     print("Count of seq start with", ori_N, "is the same number", count)
    # in case you want to store this to a list:
    if count == ori_N:
        equal_list.append(ori_N)  # to add value to list, use the function append()

    # this if block is to count the max step of all 100 sequences
    if count > max_step:
        max_step = count
        max_step_N = ori_N

    # this will print out the count for each sequence
    # print("Count of seq start with", ori_N, "is", count)

# answer for question 1
print("Max step:", max_step, "- seq:", max_step_N)

# answer for question 2
print("Max N:", max_N, "- seq:", max_N_seq)

# answer for question 3
print("List of sequence with the same number of steps as the starting N:", equal_list)

"""
I don't add the table printing to the previous code so it won't confuse you guys.
There are multiple ways to print out table format.
Some python modules (pandas or tabulate) can do it easily.
But here is how you do it with just native Python
"""

# I use the string .format() function, to read more about it: https://www.w3schools.com/python/ref_string_format.asp

# print the header
print("+----------+----------+")
print("| {:^8} | {:^8} |".format('N', 'Count'))
print("+----------+----------+")
for N in range(1, 101, 1):
    ori_N = N
    count = 0
    while True:
        if N == 1:
            break
        if N % 2 == 0:
            N = N / 2
        else:
            N = N * 3 + 1
        count += 1
    print("| {:^8} | {:^8} |".format(str(ori_N), str(count)))
# print the footer line
print("+----------+----------+")
