class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack:
                if char.isupper() and stack[-1].islower() and char.lower()==stack[-1]:
                    stack.pop()
                    continue
                elif char.islower() and stack[-1].isupper() and char.upper()==stack[-1]:
                    stack.pop()
                    continue
            stack.append(char)
        return ''.join(stack)

