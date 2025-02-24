"""Q27 String is given (paragraph type). Count the frequency of each word in string and print it."""

import re

def word_frequency_manual(s):
    s = s.lower()
    s = re.sub(r'[^\w\s]', '', s)
    words = s.split()
    
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1  # Increment count
    
    return freq_dict

# **Test Cases**
print(word_frequency_manual("This is a test. This test is just a test."))  
# print(word_frequency_manual(s2))  
# print(word_frequency_manual(s3))  
