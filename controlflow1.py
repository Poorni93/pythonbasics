menu = {"vada": 5, "pongal": 50, "dosa": 30, "idly": 20}
stack = {"vada": 10, "pongal": 20, "dosa": 10, "idly": 15}
money = 0

def order_food(food_item, quantity):
    global money
    if stack[food_item] >= quantity:
        stack[food_item] -= quantity
        money += menu[food_item] * quantity
    else:
        print(f"Sorry, not enough {food_item} in stock.")

while True:
    a = input("If you need to order any food, type y/Y or n/N: ").lower()
    
    if a == "y":
        print("Order menu: 1. vada 2. pongal 3. dosa 4. idly")
        ordered = int(input("What do you want (1-4): "))
        
        if 1 <= ordered <= 4:
            food_items = list(menu.keys())
            food_item = food_items[ordered - 1]
            quantity = int(input(f"How many {food_item}s would you like? "))
            order_food(food_item, quantity)
        else:
            print("Invalid option, please select a number between 1 and 4.")
    else:
        print(f"Total amount: {money}")
        break
