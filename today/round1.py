Numbers = [1,2,3,4,5,6,7,8,9,10]  # The list of numbers from 1 to 10

Result = []  # An empty list to store the numbers that meet a specific condition

# Calculate the average of the numbers in the list
# sum(Numbers) gives the total of all numbers in the list, which is 55
# len(Numbers) gives the number of items in the list, which is 10
# sum(Numbers) / len(Numbers) is 55 / 10, which is 5.5
average = sum(Numbers) / len(Numbers)  # So, the average is 5.5

# Now loop through each 'Number' in the 'Numbers' list
for Number in Numbers:
    
    # Check if the current 'Number' is greater than the average (5.5)
    if Number > average:
        # If it is, add it to the 'Result' list
        Result.append(Number)

# After the loop, Result will contain only the numbers greater than 5.5
print(Result)