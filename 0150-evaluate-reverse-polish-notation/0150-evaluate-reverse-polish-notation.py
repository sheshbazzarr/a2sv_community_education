from typing import List
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(x / y),  # Ensure integer division truncates towards 0
        }
        
        for char in tokens:
            if char not in operations:  # If it's a number, push to the stack
                stack.append(int(char))
            else:  # If it's an operator, pop two numbers and apply the operation
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                result = operations[char](a, b)
                stack.append(result)  # Push the result back to the stack
        
        # The final result will be the only element left in the stack
        return stack.pop()
