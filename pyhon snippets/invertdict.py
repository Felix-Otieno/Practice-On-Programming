from collections import defaultdict

# Original dictionary
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Scenario 1: Inverting when all values are unique
try:
    my_inverted_dict_unique = dict(map(reversed, my_dict.items()))
    print("Inverted dictionary with unique values:", my_inverted_dict_unique)
except TypeError:
    print("Inversion failed: non-hashable values detected.")

# Scenario 2: Inverting when values are non-unique
my_inverted_dict_non_unique = defaultdict(list)
for k, v in my_dict.items():
    my_inverted_dict_non_unique[v].append(k)
print("Inverted dictionary with non-unique values:", dict(my_inverted_dict_non_unique))

# Scenario 3: Inverting when values are non-hashable
try:
    # Example with non-hashable value (list)
    my_dict_with_non_hashable = {
        "brand": ["Ford", "Chevy"],
        "model": "Mustang",
        "year": 1964
    }
    my_inverted_dict_non_hashable = {value: key for key in my_dict_with_non_hashable for value in my_dict_with_non_hashable[key]}
    print("Inverted dictionary with non-hashable values:", my_inverted_dict_non_hashable)
except TypeError:
    print("Inversion failed: non-hashable values detected.")
