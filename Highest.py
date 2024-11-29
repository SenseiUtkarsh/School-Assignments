print('Replacting Max function!')
L = [ 19 , 25 , 36 , 56 , 102552 , 113 , 45 , 1156]
# print(max(L)) 
highest = 0
a = list()
for i in L:
    # print(i)
    if i > highest:
        highest = i
        a.append(highest)
print(highest)
print(a)