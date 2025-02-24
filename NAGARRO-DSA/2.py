"""Q1 Given a starting point in a 2D array of XY size, 
You have to rotate subarray of size N starting from given starting point.

Given:

input
1   2   3   4
5   6   7   8
9  10  11  12
13 14  15  16

output-
1   2   3   4
5   8  12  16
9   7  11  15
13  6  10  14"""

class Solution:
    def rotate90degree(self,matrix,x,y,n):
        # step 1: Transpose the sub-matrix
        for i in range(n):
            for j in range(i+1,n):
                matrix[x+i][y+j],matrix[x+j][y+i] = matrix[x+j][y+i],matrix[x+i][y+j]

        # reverse
        for j in range(n):
            for i in range(n//2):
                matrix[x+i][y+j],matrix[x+n-1-i][y+j] = matrix[x+n-1-i][y+j],matrix[x+i][y+j]
        
        return matrix



# Example matrix


s = Solution()
a = s.rotate90degree([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]],1,1,3)
print(a)
