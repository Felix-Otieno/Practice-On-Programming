# Original list of colors
mylist = ['blue', 'orange', 'green']

# Create a new list of values (e.g., the length of each color)
itr = mylist
fn = len  # Function to get the length of each color

# Using map, zip, and dict to create the dictionary
mapped_dict = dict(zip(itr, map(fn, itr)))

# Output the dictionary
print(mapped_dict)
