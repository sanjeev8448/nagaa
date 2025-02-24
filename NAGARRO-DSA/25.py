"""Q28 Given 2 sorted array and a number N. Find 2 numbers whose sum is closest to
that given number N."""

def closest_pair(arr1, arr2, N):
    i, j = 0, len(arr2) - 1
    min_diff = float('inf')
    closest_pair = (-1, -1)

    while i < len(arr1) and j >= 0:
        current_sum = arr1[i] + arr2[j]
        diff = abs(current_sum - N)

        if diff < min_diff:
            min_diff = diff
            closest_pair = (arr1[i], arr2[j])

        if current_sum > N:
            j -= 1  # Decrease sum
        else:
            i += 1  # Increase sum

    return closest_pair

# **Test Cases**
arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]

print(closest_pair(arr1, arr2, 32))  # Output: (7, 30)
print(closest_pair(arr1, arr2, 25))  # Output: (5, 20)
print(closest_pair(arr1, arr2, 50))  # Output: (7, 40)
