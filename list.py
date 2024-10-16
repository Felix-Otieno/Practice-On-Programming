myList = [10, 20, 30, 40, 50, 60]
print(myList[1])
print(tuple(myList))

tuple = tuple(myList)
print(tuple)
str_result = ''.join(map(str, myList))  # Convert each integer to a string
print(str_result)

