class Solution:
    def isValid(self, s: str) -> bool:
        match = {"[":"]","(":")","{":"}"}
        stack =[]
        for char in s:
            if char in match:
                stack.append(char)
            elif len(stack) == 0 or match[stack.pop()] != char:
                return False
        return len(stack) == 0