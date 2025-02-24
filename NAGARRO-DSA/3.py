"""Q2 There are a lot of strings like 'ab', 'bc', 'cd', 'ad' 
and you have to find the largest string can be made like ab+bc+cd = abcd (output->4), 
but keep in mind that ending character of first string should be first character of next string."""

class Solution:
    def longestStr(self,strings):
        strings.sort(key=len)  # Sort by length
        dp = {}  # Memoization
        
        max_chain = 0
        for s in strings:
            dp[s] = len(s)
            for prev in dp:
                if prev[-1] == s[0]:  # Check if it can be appended
                    dp[s] = max(dp[s], dp[prev] + len(s) - 1)
            max_chain = max(max_chain, dp[s])
        
        return max_chain

        
    
s = Solution()
# a = s.longestStr(["abc", "cde", "efg", "xyz"]) 
# a = s.longestStr(["ab", "bc", "cd", "ad"]) 

# a = s.longestStr(["ba", "ab", "bc", "cd", "de"]) 
a = s.longestStr(["xy", "yz", "zx"]) 


print(a)