import random
num = [i for i in range(1,101)]
generatedNum = random.choice(num)
print(generatedNum)
while True :
    guessedNum = int(input("Enter the number : "))
    print(guessedNum)
    if guessedNum == generatedNum :
        print("Yeh! You won...")
        break
    elif guessedNum > generatedNum :
        print("Too greater")
        False
    elif guessedNum < generatedNum :
        print("Too low!")
        False
    else:
        print('Please check Input!')
        false 