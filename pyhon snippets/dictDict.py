# Method 1: Using update() method
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merging dict2 into dict1
dict1.update(dict2)
print("Merged using update():", dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Resetting dict1 for the next example
dict1 = {'a': 1, 'b': 2}

# Method 2: Using ** (double asterisk) operator
merged_dict = {**dict1, **dict2}
print("Merged using **:", merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Method 3: Using | (pipe) operator (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1 | dict2
print("Merged using |:", merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Method 4: Using a loop to merge multiple dictionaries
dict1 = {'a': 1}
dict2 = {'b': 2}
dict3 = {'c': 3}

merged_dict = {}
for d in [dict1, dict2, dict3]:
    merged_dict.update(d)

print("Merged using loop:", merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

