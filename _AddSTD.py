# program to write data of std in text file 
f = open('Marks.txt' , 'w')
name = input('Enter your Name :')
roll = int(input('Enter roll number '))
mks = int(input('Marks '))
rec = name + str(roll) + str(mks) 
print("Data Added Successfully in text file")
f.write(rec)
f.close()