class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0

        for char in s:
            if char=='(':
                stack.append(char)
                max_depth=max(max_depth,len(stack))
            elif char ==")":
                stack.pop()
        return max_depth
    