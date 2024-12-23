def ternary_search_best_case(arr, target):
    if arr[0] == target:
        return 0
    if arr[-1] == target:
        return len(arr) - 1
   
    left, right = 0, len(arr) - 1
   
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
       
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
       
        if target < arr[mid1]: right = mid1 - 1 
        
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
   
    return -1

# Example Usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 1
print("Index of", target, ":", ternary_search_best_case(arr, target))