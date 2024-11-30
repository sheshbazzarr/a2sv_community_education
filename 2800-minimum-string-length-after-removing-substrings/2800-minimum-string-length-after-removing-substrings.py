class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            stack.append(char)

            if len(stack)>1:
                if stack[-2:]==['A','B']:
                    stack.pop()
                    stack.pop()
                elif stack[-2:]==['C','D']:
                    stack.pop()
                    stack.pop()
        return len(stack)
                

