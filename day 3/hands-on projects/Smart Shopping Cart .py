# Project 2: Smart Shopping Cart 🛒
# Concepts: Nested Dictionaries, List Comprehensions
# Enhancement Ideas:
def add_item(cart, items):
    item = input("Item name: ").lower()
    
    if item in items:
        price = float(items[item].replace('$', ''))
        print(f"✔️  Found {item} in stock at ${price:.2f}")
    else:
        print("❌ Item not found in stock. Please enter a custom price.")
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
items = {
    'earbuds': '25$',
    'iphone': '500$',
    'microphone': '13$',
    'macbook': '750$',
    'bread': '0.5$',
}

# Create header
print(f"{'| Item':<15}| {'Price |':<10}")
print("-" * 26)

# Sort by price (optional)
sorted_items = sorted(items.items(), key=lambda x: float(x[1].replace('$', '')))

# Print each row
for name, price in sorted_items:
    print(f"| {name.capitalize():<13}| {price:<7}|")

# Main program
shopping_cart = {}
while True:
     
    print(f"\n  Options: 1. Add Item 2. Checkout")
    if input("Choice: ") == "1":
        add_item(shopping_cart,items)
    else:
        checkout(shopping_cart)
        break

# Apply discounts (e.g., "Buy 2 get 1 free")

# Save receipt to a file
# Pro Tip: Try combining these projects - e.g., add a "wishlist" feature to the library manager using the shopping cart logic!