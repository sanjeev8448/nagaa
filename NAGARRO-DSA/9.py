"""Q9 Given a test string and a sample string.
Find if the characters of the sample string is in the same order in the test string. Give a simple algo.
T.S. : abcnjhgahgjhfhaljhrkhgrbhjbevfho
S.S.: nagarro"""

class Solution:
    def wordApperar(self,test,sample):
        i,j = 0,0

        while i < len(test) and j < len(sample):
            if test[i] == sample[j]:
                j += 1
            i += 1
        return j == len(sample)

s = Solution()
a = s.wordApperar("abcnjhgahgjhfhaljhrkhgrbhjbevfho","nagarro")
print(a)
