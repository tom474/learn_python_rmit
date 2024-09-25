# Challenge exercise: The Collatz Sequence

# Define variables to track the maximum values
max_step = 0
max_step_N = 0
max_N = 0
max_N_seq = 0
equal_list = []

# Main loop to iterate through numbers 1 to 100
for N in range(1, 101):
    ori_N = N
    count = 0

    # Collatz sequence calculation
    while True:
        if N > max_N:
            max_N = N
            max_N_seq = ori_N

        if N == 1:
            break

        if N % 2 == 0:
            N = N / 2
        else:
            N = N * 3 + 1

        count += 1

    # Store sequences where number of steps equals the starting number
    if count == ori_N:
        equal_list.append(ori_N)

    # Track the sequence with the maximum steps
    if count > max_step:
        max_step = count
        max_step_N = ori_N

# Output results
print("Max steps:", max_step, "- Sequence starting with:", max_step_N)
print("Max N:", max_N, "- Sequence starting with:", max_N_seq)
print("List of sequences with the same number of steps as the starting N:", equal_list)

# Printing the table with native Python
print("+----------+----------+")
print("| {:^8} | {:^8} |".format('N', 'Count'))
print("+----------+----------+")

for N in range(1, 101):
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

print("+----------+----------+")
