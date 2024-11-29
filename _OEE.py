try:
    cost_price = float(input("Enter the cost price: "))
    selling_price = float(input("Enter the selling price: "))
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100

except:
    print('Invalid Input!..')
else:
    if selling_price < cost_price:
        print("Sorry! You have lost ",loss_percentage, "%")
    if selling_price > cost_price :
        print("No loss. The selling price is higher than or equal to the cost price.")
