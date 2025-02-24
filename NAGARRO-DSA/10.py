"""Q10 Check if binary conversion of given number is palindrome or not.
6 -> 0110 - is palindrome"""


class Solution:
    def is_bin_pali(self,N):
        binary_str = bin(N)[2:]  # Convert to binary and remove "0b" prefix
        return binary_str == binary_str[::-1]

s = Solution()
a = s.is_bin_pali(8)
print(a)