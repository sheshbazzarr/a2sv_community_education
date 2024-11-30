class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and ((char.isupper() and stack[-1].islower() and char.lower() == stack[-1]) or (char.islower() and stack[-1].isupper() and char.upper() == stack[-1])):
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
