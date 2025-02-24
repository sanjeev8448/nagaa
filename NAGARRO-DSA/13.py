"""Q14 Write a program to print given matrix in wave like form.
Input:
0 1 2 3 4 
5 6 7 8 9
10 11 12 13 14
Output: 0 5 10 11 6 1 2 7 12 13 8 3 4 9 14"""

class Solution:
    def wave_print(self,matrix):
        if not matrix or not matrix[0]:
            return []
        r,c = len(matrix),len(matrix[0])
        res = []

        for j in range(c):
            if j % 2 == 0:
                for i in range(r):
                    res.append(matrix[i][j])
            else:
                for i in range(r-1,-1,-1):
                    res.append(matrix[i][j])
        return res
    
s = Solution()
a = s.wave_print([
    [0,  1,  2,  3,  4],
    [5,  6,  7,  8,  9],
    [10, 11, 12, 13, 14]
])
print(a)

