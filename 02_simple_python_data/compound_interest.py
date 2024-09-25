# Exercise 5: Compound Interest

P = float(input("Initial investment: "))
r = float(input("Annual interest rate (as a decimal): "))
n = int(input("Number of times interest is compounded per year: "))
t = int(input("Number of years: "))

# Calculate compound interest
final_amount = P * (1 + r / n) ** (n * t)

# Output the final result
print(f"Final amount after {t} years: {final_amount}")
