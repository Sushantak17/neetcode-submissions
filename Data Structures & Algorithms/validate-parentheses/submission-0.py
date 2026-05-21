class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")","{":"}","[":"]"}
        stack = []
        for char in s:
            if char in d:
                stack.append(char)
            elif stack == [] or char != d[stack.pop()]:
                return False
        return True if stack == [] else False