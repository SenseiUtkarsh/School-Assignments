import pickle
f = open('std.dat','wb')
name = input('Enter your Name :')
roll = int(input('Enter roll number '))
mks = int(input('Marks '))
rec = [name , roll ,  mks ] 
pickle.dump(rec , f)
print('Successfully Added!..')
f.close()