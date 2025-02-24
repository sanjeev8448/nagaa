"""Q4 Given a string consisting of various words Reverse all the string and words by 2 methods.
give me different approaches and test more test cases with time and space complexity"""

class Solution:
    def revW(self,word):
        return word[::-1]

s = Solution()
a = s.revW("I Love Programming")
print(a)  # Output: "gnimmargorP evoL I"


class Solution:
    def revW(self,word):
        return ''.join(reversed(word))

s = Solution()
a = s.revW("I Love Programming")
print(a)  # Output: "gnimmargorP evoL I"


class Solution:
    def revW(self,word):
        return ' '.join(word.split()[::-1])

s = Solution()
a = s.revW("I Love Programming")
print(a) # Output: "Programming Love I"

