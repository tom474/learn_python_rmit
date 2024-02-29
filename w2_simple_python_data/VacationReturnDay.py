# Exercise 4: Vacation return day

"""
General note: don't leave extra whitespaces when you type the input or string comparison will fail.
This means "friday " or " friday" are not acceptable.
To strip the white spaces, you can add the function .strip() as in below
"friday ".strip() == "friday"
"""

# In case you want to limit the number of characters input by user, use this block of code
# while True:
#     start_day = input("Start day (limit 10 chars) ").lower().strip()
#     if len(start_day) > 10:
#         print("Make it shorter. Your input length is ", str(len(start_day)))
#     else:
#         break

# In case you don't want to limit it, keep it simple like this
# get start day and lower case, if you want upper case, use the function upper()
# strip() function will remove the whitespaces
start_day = input("Start day: ").lower().strip()
duration = input("Duration: ")  # get the duration from user

# define a dictionary of days, dict in python is defined with curly brackets {}
days_dict = {
    'sunday': 0,  # the one before the : is the key, after the : is the value of each dict item
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6  # note: don't need comma "," at the last dict item
}

# loop through the dict using the key to convert the day str to number
for key in days_dict:
    if key == start_day:
        start_day = days_dict[key]  # days_dict[key] will get you the value of the dict at the current "key"
        break # you can break early

# other way with both key and value:
# for key, value in days_dict.items(): # you have to use .items() here for it to work
#     if key == start_day:
#         start_day = value
#         break

return_day = (int(start_day) + int(duration)) % 7  # calculation, can convert to int() here or at the input above

# loop through the dict using the key to convert number to day str
for key, value in days_dict.items(): # you have to use .items() here for it to work
    if return_day == value:
        return_day = key
        break

print('Return day:', return_day)
