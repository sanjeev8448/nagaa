"""Q3 Given an array of size m*n and every row of array is sorted and contains unique elements but different rows can contain same elements. 
You have to sort the array and remove the duplicates and store in 1D array.
give me different approaches and test more test cases with time and space complexity"""

class Solution:
    def freqnum(self,matrix):
        freq_map = {}
        for row in matrix:
            for num in row:
                freq_map[num] = 1 + freq_map.get(num,0) 
        return sorted(freq_map.keys())
    
s = Solution()
a = s.freqnum( [
    [1, 3, 5],
    [2, 3, 6],
    [1, 4, 7]
])
print(a)

class Solution:
    def freqnum(self,matrix):
        flat_list = [num for row in matrix for num in row]
        return sorted(set(flat_list))
    
s = Solution()
a = s.freqnum( [
    [1, 3, 5],
    [2, 3, 6],
    [1, 4, 7]
])
print(a)

