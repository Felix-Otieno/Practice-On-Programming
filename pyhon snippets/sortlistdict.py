dicts_lists = [
    {"Name": "James", "Age": 20},
    {"Name": "May", "Age": 14},
    {"Name": "Katy", "Age": 23}
]

# 1. Sorting by Age using the sort method
dicts_lists.sort(key=lambda item: item.get("Age"))
print("Sorted by Age:")
print(dicts_lists)

# 2. Sorting by Name using itemgetter
from operator import itemgetter
f = itemgetter('Name')
dicts_lists.sort(key=f)
print("\nSorted by Name:")
print(dicts_lists)
