"""Q16 Write a function to find the increasing subsequence whose sum is highest in which each number is greater than previous by 1 in thegiven array. 
If diff is less than or greater than 1 then it is not considered as subsequence. Print subsequence array and its sum. Do it in O(n).
Input: 1,2,4,5,3,4,5,6,7,9,11,12,8,9,21,35,36,37,22
Output: 35,36,37 Sum = 106"""

class Solution:
    def longestConsecutive(self, arr):
        # arr.sort()
        max_sum = float('-inf')
        max_seq = []
        
        curr_sum = arr[0]  # Current subsequence sum
        curr_seq = [arr[0]]  # Current subsequence
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1] + 1:  # Check for increasing sequence with difference 1
                curr_seq.append(arr[i])
                curr_sum += arr[i]
            else:
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    max_seq = curr_seq[:]
                
                curr_sum = arr[i]  # Reset for new sequence
                curr_seq = [arr[i]]

        # Final check for the last subsequence
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_seq = curr_seq
        return max_seq, max_sum
    
s = Solution()
a = s.longestConsecutive([1,2,4,5,3,4,5,6,7,9,11,12,8,9,21,35,36,37,22])
print(a)