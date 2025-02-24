"""Q7 You are given a sorted array containing both negative and positive values. 
Resort the array taking absolute value of negative numbers.
Your complexity should be O(n)."""

# class Solution:
#     def sArray(self,arr):
#         return sorted(arr,key=abs)

# s = Solution()
# a = s.sArray([-9, -5, -3, -1, 2, 4, 6, 8])
# print(a) # Output: [-1, 2, -3, 4, -5, 6, -9, 8]


class Solution:
    def sArray(self,arr):
        return sorted(arr,key=abs)

s = Solution()
a = s.sArray([-9, -5, -3, -1, 2, 4, 6, 8])
print(a) # Output: [-1, 2, -3, 4, -5, 6, -9, 8]