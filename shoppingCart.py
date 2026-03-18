foods = [] #We can use set as well, but since sets are unordered and unchangable, we are using List here
prices = []
total = 0


while True:
    food = input("Enter the food you want to add (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("Enter the price of the food: "))
        foods.append(food)
        prices.append(price)

print("----YOUR CART----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nYour total is: ₹{total}.")
    