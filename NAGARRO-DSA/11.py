"""Q11 Given an unsorted array. Find the 4th largest element in it in O(n) time complexity."""

class Solution:
    def fourthlarges(self,arr):
        arr.sort()
        return arr[-4]
s = Solution()
a = s.fourthlarges([3, 1, 5, 6, 9, 2, 8, 7, 4])
print(a)



import heapq

class Solution:
    def fourthLargest(self, arr):
        if len(arr) < 4:
            return "Not enough elements"

        minHeap = []
        for num in arr:
            heapq.heappush(minHeap, num)
            if len(minHeap) > 4:
                heapq.heappop(minHeap)  # Remove smallest element

        return heapq.heappop(minHeap)  # 4th largest element

# Testing
s = Solution()
arr = [3, 1, 5, 6, 9, 2, 8, 7, 4]
print(s.fourthLargest(arr))  # Output: 6