class Solution:
    def isValid(self, s: str) -> bool:
        values = {")":"(","}":"{","]":"["}
        stack = []
        for c in s:
            if not c in values:
                stack.append(c)
            elif stack and stack[-1] == values[c]:
                stack.pop()
            else:
                return False
        return False if stack else True 