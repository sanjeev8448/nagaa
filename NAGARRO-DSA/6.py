"""Q5 Given 2 sorted arrays of size N and 2N.
Merge these sorted arrays and remove duplicates (if any). 
The resultant array should be in sorted order.
Do this by 3 methods."""

class Solution:
    def Sarray(self,arr1,arr2):
        arr3 = (arr1 + arr2)
        arr3.sort()
        return set(arr3)

s = Solution()
a = s.Sarray([1, 3, 5, 7],[2, 3, 6, 7, 8, 9])
print(a) # Output: [1, 2, 3, 5, 6, 7, 8, 9]

class Solution:
    def Sarray(self,arr1,arr2):
        return sorted(set(arr1) | set(arr2))

s = Solution()
a = s.Sarray([1, 3, 5, 7],[2, 3, 6, 7, 8, 9])
print(a) # Output: [1, 2, 3, 5, 6, 7, 8, 9]


def merge_in_place(arr1, arr2):
    arr1.extend(arr2)  # Merge two arrays
    arr1.sort()  # Sort the merged array

    # Remove duplicates in-place
    i = 1
    while i < len(arr1):
        if arr1[i] == arr1[i - 1]:
            arr1.pop(i)
        else:
            i += 1
    return arr1