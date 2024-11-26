class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """ 
            Calculate the score of a balanced parentheses string.]
            
            Rules:
            - "()" has a score of 1.
            - "AB"(wher A and B are valid parentheses strings) has a score of A+B.     
            - "(A)" has a score of 2*A.


            Args:
            s (str):The input string consisting of '('  and ')'.

            Returns:
            int: The score of the parentheses string.
        """
            #    Stack to store intermediate scores 
        stack=[]
        # The final output score 
        output = 0
        # Iterate through each character in the string
        for char in s:
            if char =="(":
                # Push a zero onto the stack to represent the start of a new scope
                stack.append(0)
            elif char ==")":
                # Pop the top value from the stack 
                top = stack.pop()

                # if the top value is zero , it means the scop is "()" , which has a score of 2
                if top == 0:
                    score =1
                elif top>0:
                    # Otherwise, double the score of the inner scope
                    score = top*2
                if not stack:
                    # if the stack is empty, it means this score belongs 
                    # to the outermost level
                    output+=score
                elif stack:
                    # Otherwise, add this score to the last element in the stack
                    stack[-1]+=score
        return output

