items = [
    {'name': 'Apple', 'price': 100, 'quantity': 5},
    {'name': 'Banana', 'price': 50, 'quantity': 3},
    {'name': 'Banana', 'price': 60, 'quantity': 2},
    {'name': 'Apple', 'price': 80, 'quantity': 4}
]

# Sort by name, then by price, and then by quantity
sorted_items = sorted(items, key=lambda x: (x['name'], x['price'], x['quantity']))

print(sorted_items)
