def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"HCF of {x} and {y} is {hcf(x, y)}")
