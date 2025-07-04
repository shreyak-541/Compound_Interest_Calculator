def compound_interest_calculator(principal, rate_of_interest, no_of_years):
    amount = principal * (((1) + rate_of_interest/100) ** no_of_years)
    compound_interest = amount - principal
    return (amount, compound_interest)

print("                 Compound Interest Calculator                 ")
print("\n------------------------------------------------------------")

p = float(input("Enter Principal Amount(₹): "))
r = float(input("Enter Annual Rate of Interest(%): "))
n = float(input("Enter time period (in years) :"))

a,ci = compound_interest_calculator(p, r, n)

print(f"Compound Interest: ₹{ci:.2f}")
print(f"Total Amount after Interest: ₹{a:.2f}")

