try:
    cost_price = float(input("Enter the cost price: "))
    selling_price = float(input("Enter the selling price: "))
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
except:
    print("Invalid Input!")
else:
    print("You gaind profit of ",profit_percentage ,"%")
finally:
    print('Thanks for using this App!')