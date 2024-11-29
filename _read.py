import pickle
print("Read data of Binary file.")
f = open('std.dat','rb')
data = pickle.load(f)
for i in data:
    print(i)
f.close()