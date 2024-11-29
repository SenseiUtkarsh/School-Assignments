# TIP CALCULATOR -
print('Welcome to tip calculator!')
bill = float(input('What was the total bill? $' ))
tip = int(input('What percentage  tip would you like to give? 10, 12, or 15? '))
sp = int(input('How many people to split the bill?'))
per = tip * bill /100
result = round(( bill + per ) / sp , 2 ) # to round upto 2 digit
print(f'Each person should pay: ${result}')