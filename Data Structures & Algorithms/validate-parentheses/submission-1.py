class Solution:
    def isValid(self, s: str) -> bool:
        #guardar en una pila acumulando las abiertas para luego ir popeando las cerradas a ver si corresponden
        cerradas = {"}":"{","]":"[",")":"("}
        stack = []

        for c in s:
            if c in cerradas:
                if stack and stack[-1] == cerradas[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
            
            