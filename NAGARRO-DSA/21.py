"""Q23 Given a string containing characters and brackets. Find if brackets are paired or not."""

def is_balanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  # Opening brackets
            stack.append(char)
        elif char in bracket_map.keys():  # Closing brackets
            if not stack or stack.pop() != bracket_map[char]:
                return False
    return len(stack) == 0

# **Test Cases**
print(is_balanced("{[()()]}"))   # True
print(is_balanced("{[(])}"))     # False
print(is_balanced("abc[d]ef(g)"))# True
print(is_balanced("{[}"))        # False
print(is_balanced("((()))"))     # True
