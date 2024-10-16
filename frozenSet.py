# Creating a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])

# Displaying the frozenset
print("Frozenset:", my_frozenset)

# Trying to add an element will raise an AttributeError
try:
    my_frozenset.add(6)  # This will fail
except AttributeError as e:
    print("Error:", e)

# You can still perform set operations
another_frozenset = frozenset([4, 5, 6, 7])

# Union
union_set = my_frozenset | another_frozenset
print("Union:", union_set)

# Intersection
intersection_set = my_frozenset & another_frozenset
print("Intersection:", intersection_set)

# Difference
difference_set = my_frozenset - another_frozenset
print("Difference:", difference_set)

# Checking membership
print("Is 3 in my_frozenset?", 3 in my_frozenset)
