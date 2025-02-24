"""You are given an array of 0s and 1s in random order. 
Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the array]. 
Traverse array only once. 

Input :  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output :  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] """


# Approach 1: Counting 0s and 1s (O(n) Time, O(1) Space)
class Solution:
    def inplace(self,arr):
        count_zeroes = arr.count(0)
        return [0]*count_zeroes + [1]*(len(arr)-count_zeroes)
    
s = Solution()
a = s.inplace([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])
print(a)


# Approach 2: Two-Pointer Method (O(n) Time, O(1) Space)
class Solution:
    def inplace(self,arr):
        l,r = 0,len(arr)-1
        while l < r:
            while l < r and arr[l] == 0:
                l += 1
            while l < r and arr[r] == 1:
                r -= 1
            if l < r:
                arr[l],arr[r] = arr[r],arr[l]
                l,r = l+1,r-1
        return arr

s = Solution()
a = s.inplace([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])
print(a)


#Approach 3: Dutch National Flag Algorithm (O(n) Time, O(1) Space)
class Solution:
    def inplace(self,arr):
        low = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[low],arr[i] = arr[i],arr[low]
                low += 1
        return arr
        
s = Solution()
a = s.inplace([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])
print(a)
    



