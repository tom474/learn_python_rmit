# Exercise 5: Compound interest
P = float(input("Initial investment: "))
r = float(input("Interest rate: "))
n = int(input("Number of compound times per year: "))
t = int(input("Number of years: "))

output = P * (1+r/n)**(n*t)
print("Final output:", output)
