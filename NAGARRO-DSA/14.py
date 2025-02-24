"""Q15 Write a function to check if the given string contains the given number of unique character. 
R & r should be counted as same character.
Input: Nagarro is best software company, N = 17
output - True or False"""
from collections import defaultdict
class Solution:
    def has_exactly_n_unique(self,s,N):
        unique_chr = set(c.lower() for c in s if c.isalpha())
        return len(unique_chr) == N

s = Solution()
# a = s.has_exactly_n_unique("Nagarro is best software company", 17)
a = s.has_exactly_n_unique("Hello World", 7)
print(a)

class Solution:
    def has_exactly_n_unique(self,s,N):
        char_cnt = defaultdict(int)
        for char in s:
            if char.isalpha():
                char_cnt[char.lower()] += 1
        return len(char_cnt) == N


s = Solution()
a = s.has_exactly_n_unique("Nagarro is best software company", 17)
# a = s.has_exactly_n_unique("Hello World", 7)
print(a)

