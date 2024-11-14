Numbers = [1,2,3,4,5,6,7,8,9,10]

Result = [Number for Number in Numbers if Number > sum(Numbers)/len(Numbers)]

print(Result)