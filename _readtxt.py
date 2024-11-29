print("Read data of text file..")
f = open('Marks.txt','r')
lines = f.readlines()
for data in lines:
    print(data , end=" ")
    f.close()
