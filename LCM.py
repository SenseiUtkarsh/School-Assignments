import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Example usage:
num1 = int(input('Enter 1st Number : '))
num2 = int(input('Enter 2nd Number : '))
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")