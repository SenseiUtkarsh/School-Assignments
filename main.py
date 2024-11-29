import Module as mod

print("Divine Sainik School")
print("Lahartara , Varanasi , UP")
mod.MENU()
while True :
    choice = int(input("Enter Your Choice\n"))
    if choice == 1:
        mod.AddSt()
    elif choice == 2:
        mod.RemoveSt()
    elif choice == 3:
        mod.SearchStd()
    elif choice == 4:
        mod.SubmitFee()
    elif choice == 5:
        mod.AddTeacher()
    elif choice == 6:
        mod.RemoveTec()
    elif choice == 7:
        mod.UpdateSa()
    else:
        print("Invalid Input!...")
    ch = input("Do You Want to proceed futher? T or F ").capitalize()
    print(ch)
    if ch == "F" :
        print("Thank You! Have a great day..")
        break




