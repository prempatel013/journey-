def add_item(cart):
    item = input("Item name: ")
    price = float(input("Price: $"))
    quantity = int(input("Quantity: "))
    
    if item in cart:
        cart[item]["quantity"] += quantity
    else:
        cart[item] = {"price": price, "quantity": quantity}

def checkout(cart):
    print("\n🧾 RECEIPT:")
    total = 0
    for item, details in cart.items():
        subtotal = details["price"] * details["quantity"]
        print(f"{item} x{details['quantity']}: ${subtotal:.2f}")
        total += subtotal
    
    print(f"\nTOTAL: ${total:.2f}")
    return total

# Main program
shopping_cart = {}
while True:
    print("\nOptions: 1. Add Item 2. Checkout")
    if input("Choice: ") == "1":
        add_item(shopping_cart)
    else:
        checkout(shopping_cart)
        break