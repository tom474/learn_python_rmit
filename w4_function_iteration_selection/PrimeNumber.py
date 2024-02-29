# Function definition
def is_prime(n):
    """
    takes a single integer parameter (positive) and returns True when the argument is a prime number and False otherwise
    """
    if n == 1 or n == 0:
        return False
    acc = 2  # we start at 2 because 1 is a divisor for any integer
    while acc < n:
        if n % acc == 0:
            return False
        else:
            acc = acc+1
    return True  # NOT divisible by 4, it is NOT a leap year


max_number = int(input("Up to when do you want to show prime numbers?: "))

for i in range(2, max_number):
    if is_prime(i):  # we re-use our previous code (dividing and conquering)
        print(i)
