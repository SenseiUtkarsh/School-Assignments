import csv
# add std in csv file
f = open('std.csv' , 'w')

name = input('Enter your Name :')
roll = int(input('Enter roll number '))
mks = int(input('Marks '))
rec = name + str(roll) + str(mks) 
rec = [name , roll , mks]
# for i in rec:
    # 
write = csv.writer(f)
write.writerow(rec)

print("Successfull Data added in csv file ")