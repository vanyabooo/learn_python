"""
Price of a house is $1
if good credit => put 10%
otherwise put 20%
print the down payment
"""

price = float(input(f'Please enter the price of a house that you want to buy in dollars: '))
print(f'Price of a house is ${price}')

score = input("Do you have a good credit score? Please answer yes or no: ").lower()

if score == "yes":
    print(f"Our congratulations, you down payment is ${price * 0.1}")
elif score == "no":
    print(f"Unfortunately you hgve to put ${price * 0.2}")
else:
    print("Пошел нахуй")