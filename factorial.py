# 4. Program to find factorial of a given number
num = int(input("Enter a number: " ))
fact = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers" )
elif num == 0:
    print("The factorial of 0 is 1" )
else:
    for i in range( 1 , num + 1 ):
        fact = fact * i
    print("factorial of num", " is " , fact)
