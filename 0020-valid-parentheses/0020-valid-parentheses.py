class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in parenthesis_map.values():
                # If it's an opening bracket, push to stack
                stack.append(char)
            elif char in parenthesis_map:
                # If it's a closing bracket, check if it matches the top of the stack
                if stack and stack[-1] == parenthesis_map[char]:
                    stack.pop()  # Remove the matching opening bracket
                else:
                    return False  # Mismatch or no opening bracket
            else:
                # Invalid character (if you want to handle only parentheses)
                return False

        # If the stack is empty, all parentheses were properly matched
        return not stack
