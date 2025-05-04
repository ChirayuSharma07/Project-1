# Hotel Menu Ordering Program 

# -- MENU INITIALIZATION -- #

print("🍽️ Welcome to MOM'S Restaurant!")
print("Glad to have you here!")
print("Here’s what we’re serving today:\n")

# Menu Dictionary (items sorted by categories)
menu = {
    "BIRYANI": {
        '1': {'name': 'Chicken Biryani', 'price': 50},
        '2': {'name': 'Dum Chicken Biryani', 'price': 100},
        '3': {'name': 'Paneer Biryani', 'price': 50},
        '4': {'name': 'Veg Matka Biryani', 'price': 85},
        '5': {'name': 'Egg Biryani', 'price': 70}
    },
    "PIZZA": {
        '6': {'name': 'Cheese Pizza', 'price': 69},
        '7': {'name': 'Veg Pizza', 'price': 89},
        '8': {'name': 'Farm House Pizza', 'price': 129},
        '9': {'name': 'Paneer Pizza', 'price': 129},
        '10': {'name': 'Paneer Makhani Pizza', 'price': 149},
        '11': {'name': 'Chicken Pizza', 'price': 79},
        '12': {'name': 'Chicken Cheese Pizza', 'price': 129},
        '13': {'name': 'Chicken Tandoori Pizza', 'price': 149},
        '14': {'name': 'Chicken Barbeque Pizza', 'price': 169}
    },
    "DRINKS": {
        '15': {'name': 'Coca Cola', 'price': 30},
        '16': {'name': 'Pepsi', 'price': 30},
        '17': {'name': 'Fanta', 'price': 30},
        '18': {'name': 'Sprite', 'price': 30},
        '19': {'name': 'Lemonade', 'price': 20},
        '20': {'name': 'Lassi', 'price': 50},
        '21': {'name': 'Mango Shake', 'price': 50},
        '22': {'name': 'Oreo Shake', 'price': 80},
        '23': {'name': 'Chocolate Shake', 'price': 80},
        '24': {'name': 'Lichi Shake', 'price': 100}
    }
}

# menu visible to user
print("Here’s our menu for today:\n")
for category, items in menu.items():
    print(f"\n--- {category} ---")
    for code, item in items.items():
        print(f"{code}. {item['name']} - ₹{item['price']}")  

# Get item by name you want to order
def get_item_by_name(name_input):
    name_input = name_input.strip().lower()
    for category in menu.values():
        for item in category.values():
            if item['name'].lower() == name_input:
                return item
    return None

# Start taking orders
order = []
total_amount = 0

print("\n✨ Time to place your order! ✨")

while True:      #make it infinite loop until user is done ordering
    item_input = input("Type the name of the dish you’re interested in: ").strip()
    #strip() ye code m se extra space remove krta h
     #lower() agar item ka naam match kr rha h to alphabetiic error nhi aayegi
    
    confirm = input(f"Just to confirm, you'd like to order '{item_input}'? (yes/no): ").strip().lower()
    if confirm != 'yes':
        again = input("Want to try something else? (yes/no): ").strip().lower()
        if again != 'yes':
            break
        continue

    # Check if item exists
    item_info = get_item_by_name(item_input)

    if not item_info:
        print(f"Oops! '{item_input}' isn’t on our menu right now.")
        another = input("Would you like to try ordering something else? (yes/no): ").strip().lower()
        if another != 'yes':
            break
        continue

    # How many you want? (max 5)
    while True:
        count = input(f"How many '{item_info['name']}' would you like? (Up to 5): ")
        try:
            count = int(count)
            if count <= 0:
                print("You need to order at least one.")
            elif count > 5:
                print("⚠️ Sorry, 5 is the max allowed.")
            else:
                break
        except:
            print("Invalid input. Please type a number.")

    subtotal = item_info['price'] * count

    order.append({
        'name': item_info['name'],
        'price': item_info['price'],
        'qty': count,
        'total': subtotal
    })

    total_amount += subtotal #total amount - costumer order kr reha h ve usse price bata rha h, subtotal - value ko add kr rha 
    print(f"✅ Order noted: {count} x {item_info['name']} = ₹{subtotal}")

    more = input("Want to add more to your order? (yes/no): ").strip().lower()
    if more != 'yes':
        print("Thank you for your order!")
        break          #user is done ordering

# Final bill
print("\n🧾 Your Order Summary:")
print("-" * 50)
print(f"{'Item':<25} {'Price':<7} {'Qty':<5} {'Total':<7}")
print("-" * 50)
for item in order:
    print(f"{item['name']:<25} ₹{item['price']:<6} {item['qty']:<5} ₹{item['total']:<6}")
print("-" * 50)
print(f"{'Total bill:':<39} ₹{total_amount}")
print("-" * 50)

# Thanks msg
print("\n🙏 Thank you for choosing MOM’S Restaurant!")
print("Enjoy your meal & come back soon! 😊")