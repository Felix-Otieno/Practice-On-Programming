def merge(*args, missing_val = None):
#missing_val will be used when one of the smaller lists is shorter tham the others.
#Get the maximum length within the smaller lists.
  max_length = max([len(lst) for lst in args])
  outList = []
  for i in range(max_length):
    outList.append([args[k][i] if i < len(args[k]) else missing_val for k in range(len(args))])
  return outList
print(merge([1, 2, 3], [4, 5], [6], missing_val=0))

