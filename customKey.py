# Sort a list of tuples by the second element
items = [(1, 'apple'), (3, 'banana'), (2, 'orange')]
sorted_items = sorted(items, key=lambda x: x[1])
print(sorted_items)  # Output: [(1, 'apple'), (3, 'banana'), (2, 'orange')]