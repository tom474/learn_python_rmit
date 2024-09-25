def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(mult(a, b))


main()
