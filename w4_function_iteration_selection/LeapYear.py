def check_leap_year(x):
    """
    This function will check if the year is a leap year or not
    :param x: the year(int)
    :return: True/False
    """

    # either one of these 2 is correct
    # if x % 4 == 0 and (x % 100 != 0 or (x % 100 == 0 and x % 400 == 0)):
    if ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0):
        return True
    else:
        return False


print(check_leap_year(2000))

''' alternative solution '''
# def is_leap(x):
#     ans = False
#     if x % 100 == 0:
#         if x % 400 == 0:
#             ans = True
#     else:
#         if x % 4 == 0:
#             ans = True
#     return ans
#
# print(is_leap(1900))

