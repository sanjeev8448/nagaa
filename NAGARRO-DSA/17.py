"""Q18 Print all subarray in an array whose sum is a given number.
arr = [1, 2, 3, 4, 5]
target = 5
"""

def find_subarrays_bruteforce(arr, target):
    n = len(arr)
    res = []
    for i in range(n):
        sub_sum = 0
        for j in range(i, n):
            sub_sum += arr[j]
            if sub_sum == target:
                # print(arr[i:j+1])
                res.append(arr[i:j+1])
    return res

# **Test Cases**
a = find_subarrays_bruteforce([1, 2, 3, 4, 5], 5)
print(a)

def find_subarrays_sliding_window(arr, target):
    start, sub_sum = 0, 0
    for end in range(len(arr)):
        sub_sum += arr[end]
        
        while sub_sum > target and start <= end:  # Shrink window if needed
            sub_sum -= arr[start]
            start += 1
        
        if sub_sum == target:
            print(arr[start:end+1])