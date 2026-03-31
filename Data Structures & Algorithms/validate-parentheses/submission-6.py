class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {"}":"{", "]":"[", ")":"("}
        # stack only contains opening brackets
        for c in s:
            if c in pmap:
                if stack and pmap[c] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
