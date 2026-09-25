class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        matching = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for char in s:
            if char in matching:
                if stack and stack[-1] == matching[char]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True