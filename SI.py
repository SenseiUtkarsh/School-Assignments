def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
print(f"Simple Interest: {simple_interest(p, r, t)}")
