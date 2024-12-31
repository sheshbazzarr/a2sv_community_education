class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 to handle edge cases
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '(' onto the stack
            else:
                stack.pop()  # Pop the top element from the stack
                if not stack:
                    stack.append(i)  # Push the current index as a new base
                else:
                    # Calculate the length of the current valid substring
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)

        return max_length