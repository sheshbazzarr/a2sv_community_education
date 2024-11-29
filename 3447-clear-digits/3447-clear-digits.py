class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []
        for char in s:
            if char.isdigit():
                if stack and not stack[-1].isdigit():
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)