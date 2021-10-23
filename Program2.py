apple = int(input("Enter the number of apples to be purchased: "))
apple_total = apple*20
print(f"Total amount for apples: {apple_total} pesos.")

orange = int(input("Enter the number of oranges to be purchased: "))
orange_total = orange*25
print(f"Total amount for oranges: {orange_total} pesos.")

total = apple_total + orange_total 
print(f"The total amount is {total} pesos.")