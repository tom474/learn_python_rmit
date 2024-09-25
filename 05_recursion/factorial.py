def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def main():
    n = int(input("Enter a number: "))
    print("The factorial number of", n, "is:", factorial(n))


main()
