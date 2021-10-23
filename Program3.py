money = int(input("Enter the amount of money you have on hand: "))
apple_price = int(input("Enter the price for each apple: "))

pieces_apple = money // apple_price
change = money % apple_price
print(f"You can buy {pieces_apple} apples and your change is {change} pesos.")