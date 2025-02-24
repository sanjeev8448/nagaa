"""Q24 Given a set of integers. Find the 3rd max. sum of two elements from the set.
array: 3,6,2,7,8,19,13,5
3rd max sum: 8+7 = 15"""

def third_max_sum(arr):
    arr.sort(reverse=True)  # Sort in descending order
    sums = []
    
    for i in range(len(arr) - 1):
        sums.append(arr[i] + arr[i + 1])  # Compute sums of consecutive pairs
    
    sums = sorted(set(sums), reverse=True)  # Unique and sorted sums

    return sums[2] if len(sums) >= 3 else None  # Return 3rd max sum

# **Test Cases**
print(third_max_sum([3,6,2,7,8,19,13,5]))  # Output: 15
print(third_max_sum([1, 2, 3, 4, 5]))      # Output: 5
print(third_max_sum([10, 20, 30, 40]))     # Output: 50
print(third_max_sum([100, 200]))           # Output: None (Only one sum possible)
