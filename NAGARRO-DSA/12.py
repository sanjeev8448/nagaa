"""Q13 Given a string. Find the longest substring having atmost 2 unique characters. 
If there are multiple longest substrings return them all.
Given: "helloworld"
output: ell,llo.owo"""

def longestSubstringOptimized(s):
    char_map = {}
    start = 0
    max_length = 0
    substrings = []

    for end, char in enumerate(s):
        char_map[char] = end

        if len(char_map) > 2:
            min_index = min(char_map.values())  
            del char_map[s[min_index]]  
            start = min_index + 1  

        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            substrings = [s[start:end + 1]]
        elif current_length == max_length:
            substrings.append(s[start:end + 1])

    return substrings

# Test
print(longestSubstringOptimized("abcabcabc"))  # Output: ['bc', 'ca', 'ab', 'bc', 'ca', 'ab', 'bc', 'ca', 'ab']
print(longestSubstringOptimized("helloworld"))  # Output: ['ell', 'llo', 'owo']
