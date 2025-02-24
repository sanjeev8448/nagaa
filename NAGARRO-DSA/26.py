"""Q29 Merge an array of size M into another array of size M+N."""

def merge_sorted_arrays(arr1, arr2, M, N):
    i, j, k = M - 1, N - 1, M + N - 1

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    # If any elements are left in arr2
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

    return arr1


def merge_with_sorting(arr1, arr2, M, N):
    arr1[M:] = arr2  # Replace None values
    arr1.sort()  # Sort the entire array
    return arr1

# **Test Cases**
arr1 = [2, 5, 7, None, None, None]
arr2 = [3, 6, 8]
print(merge_with_sorting(arr1, arr2, 3, 3))  # Output: [2, 3, 5, 6, 7, 8]


# **Test Cases**
arr1 = [2, 5, 7, None, None, None]
arr2 = [3, 6, 8]
M, N = 3, 3
print(merge_sorted_arrays(arr1, arr2, M, N))  # Output: [2, 3, 5, 6, 7, 8]

arr1 = [1, 4, 6, 10, None, None, None, None]
arr2 = [2, 5, 7, 9]
print(merge_sorted_arrays(arr1, arr2, 4, 4))  # Output: [1, 2, 4, 5, 6, 7, 9, 10]
