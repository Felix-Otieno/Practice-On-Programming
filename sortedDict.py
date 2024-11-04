# Sample list of dictionaries
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 30}
]

# Sorting by age
sorted_people = sorted(people, key=lambda x: x['age'])

print(sorted_people)
