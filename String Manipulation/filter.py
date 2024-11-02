text = "Hello, World! 123"
filtered_text = ''.join([char for char in text if char.isalpha() or char.isspace()])
print(filtered_text)  # Output: "Hello World"
