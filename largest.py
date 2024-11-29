def maximum(x, y, z):
    if (x >= y) and (x >= z):
        largest = x

    elif (y >= x) and (y >= z):
        largest = y

    else:
        largest = z

    return largest
print(maximum(2,9,5))
print(maximum(2,9,199))
print(maximum(20,9,1))