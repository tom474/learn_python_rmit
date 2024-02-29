def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    return not is_even(n)


def main():
    n = int(input("Enter a number: "))
    if is_odd(n):
        print("This is a odd number")
    else:
        print("This is a even number")


main()
