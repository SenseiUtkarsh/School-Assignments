# The Gauss Challange -- to find the sum of first 100 natural numbers!

n = int(input('Enter the last number of the series: '))

sum = 0
for i in range( 0 , n+1):
    sum += i

print(sum)