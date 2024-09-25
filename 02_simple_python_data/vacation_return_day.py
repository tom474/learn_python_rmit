# Exercise 4: Vacation return day

# Get the start day and duration from the user, clean the input using strip() and lower()
start_day = input("Start day: ").lower().strip()
duration = int(input("Duration (in days): "))  # Get duration as an integer

# Dictionary mapping days of the week to numbers
days_dict = {
    "sunday": 0,
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6
}

# Convert the start day to a number using the dictionary
if start_day in days_dict:
    start_day_num = days_dict[start_day]
else:
    print("Invalid day entered.")
    exit()

# Calculate the return day number
return_day_num = (start_day_num + duration) % 7

# Convert the return day number back to the day name
for day, num in days_dict.items():
    if return_day_num == num:
        return_day = day
        break

# Output the return day
print("Return day:", return_day)
