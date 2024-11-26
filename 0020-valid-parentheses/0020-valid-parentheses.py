class Solution:
    def isValid(self, s: str) -> bool:
        """ 
        Check if the input string of parentheses is valid.
        A valid string must have matching open and close parentheses in the correct order.

        :param s: A string containing only '(',')','
        """
        matching_parentheses = {")": "(", "]": "[", "}": "{"}
        stack=[]
        for char in s:
            stack.append(char)

            if char in matching_parentheses:
                if len(stack)>1 and stack[-2]==matching_parentheses[char]:
                    stack.pop()
                    stack.pop()
                else:
                    return False
            
        return not stack
        