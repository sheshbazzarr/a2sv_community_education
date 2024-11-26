class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if the input string of parentheses is valid.
        A valid string must have matching open and close parentheses in the correct order.

        :param s: A string containing only '(', ')', '{', '}', '[' and ']'.
        :return: True if the string is valid, False otherwise.
        """
        # Map of closing parentheses to their corresponding opening parentheses
        matching_parentheses = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            # Always append first
            stack.append(char)

            # Check for closing parenthesis after appending
            if char in matching_parentheses:
                # Ensure there is a valid opening parenthesis to match
                if len(stack) > 1 and stack[-2] == matching_parentheses[char]:
                    stack.pop()  # Remove the current closing parenthesis
                    stack.pop()  # Remove the matched opening parenthesis
                else:
                    return False  # Invalid match
        
        # If the stack is empty, all parentheses were matched
        return not stack
