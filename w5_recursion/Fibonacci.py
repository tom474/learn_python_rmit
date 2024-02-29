def recur_fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)


def main():
    n = int(input("Enter n: "))
    print(recur_fibo(n))


main()

