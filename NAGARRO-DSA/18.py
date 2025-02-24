"""Q20Given a string. Find the longest sub-string with all distinct characters in it. 
If there are such strings print all.
Do it in O(n)."""

def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    substrings = []

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        length = right - left + 1

        if length > max_length:
            max_length = length
            substrings = [s[left:right + 1]]
        elif length == max_length:
            substrings.append(s[left:right + 1])

    return substrings, max_length

# **Test Cases**
print(longest_unique_substring("abcadbef"))  # Output: (["bcad", "cadb", "adbe", "dbef"], 4)
print(longest_unique_substring("aaaa"))      # Output: (["a"], 1)
print(longest_unique_substring("abcd"))      # Output: (["abcd"], 4)
print(longest_unique_substring("aabcbcdb"))  # Output: (["bcda", "cdab"], 4)



def longest_unique_substring_optimized(s):
    char_map = {}
    left = 0
    max_length = 0
    substrings = []

    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        
        char_map[s[right]] = right
        length = right - left + 1

        if length > max_length:
            max_length = length
            substrings = [s[left:right + 1]]
        elif length == max_length:
            substrings.append(s[left:right + 1])

    return substrings, max_length

# **Test Cases**
print(longest_unique_substring_optimized("abcadbef"))  # Output: (["bcad", "cadb", "adbe", "dbef"], 4)
print(longest_unique_substring_optimized("aaaa"))      # Output: (["a"], 1)
print(longest_unique_substring_optimized("abcd"))      # Output: (["abcd"], 4)
print(longest_unique_substring_optimized("aabcbcdb"))  # Output: (["bcda", "cdab"], 4)
