# create a sequence from 2 to 10 with increment of 3
numbers = range(2, 10, 3)
print(list(numbers))    # [2, 5, 8]

# create a sequence from 4 to -1 with increment of -1
numbers = range(4, -1, -1)    
print(list(numbers))    # [4, 3, 2, 1, 0]

# range(0, 5, 1) is equivalent to range(5)
numbers = range(0, 5, 1) 
print(list(numbers))    # [0, 1, 2, 3, 4]