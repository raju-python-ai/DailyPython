p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (in %): "))
t = float(input("Enter time period (in years): "))

ci = p * ((1 + r / 100) ** t - 1)

print(f"Compound Interest: {ci:.2f}")
