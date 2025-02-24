"""Q21 Find all common elements in given 3 sorted arrays.
Do it in O(n) without extra space.
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output:
[20, 80]

"""

def find_common_elements_hashing(arr1, arr2, arr3):
    set1 = set(arr1)
    set2 = set()
    for num in arr2:
        if num in set1:
            set2.add(num)
    
    common_elements = []
    for num in arr3:
        if num in set2:
            common_elements.append(num)

    return common_elements

# **Test Cases**
print(find_common_elements_hashing([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120])) 
# Output: [20, 80]


