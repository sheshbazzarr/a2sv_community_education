class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      
        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                # Push numbers to the stack
                stack.append(int(token))
            else:
                # Pop the last two numbers
                b = stack.pop()
                a = stack.pop()
                
                # Apply the operator and push the result
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Perform integer division truncating toward zero
                    stack.append(int(a / b))
        
        return stack[0]
