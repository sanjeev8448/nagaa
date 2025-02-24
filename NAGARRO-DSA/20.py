"""Q22 Given an unsorted list of repeated elements Find the element with maximum frequency.
arr = [1, 3, 2, 3, 4, 1, 6, 3, 2, 1, 1]
1  (appears 4 times)
"""

from collections import Counter

def max_frequency_element(arr):
    freq_map = Counter(arr)  # Create frequency dictionary
    max_element = max(freq_map, key=freq_map.get)  # Find max frequency element
    return max_element, freq_map[max_element]

# **Test Cases**
print(max_frequency_element([1, 3, 2, 3, 4, 1, 6, 3, 2, 1, 1]))  
# Output: (1, 4)

print(max_frequency_element([5, 5, 5, 2, 2, 8, 8, 8, 8]))  
# Output: (8, 4)

print(max_frequency_element([7, 7, 7, 7, 7]))  
# Output: (7, 5)

print(max_frequency_element([1, 2, 3, 4, 5]))  
# Output: (1, 1) (all have same frequency)
