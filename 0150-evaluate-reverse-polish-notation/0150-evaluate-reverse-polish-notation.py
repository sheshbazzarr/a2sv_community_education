import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        
        :param tokens: A list of strings representing the RPN expression.
        :return: The integer result of the evaluation.
        """
        # Stack to store operands and intermediate results
        operand_stack = []
        
        # Mapping of operators to their corresponding functions
        operator_functions = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(x / y)  # Ensure truncation towards zero for division
        }
        
        for token in tokens:
            if token in operator_functions:  # If the token is an operator
                # Pop the top two operands from the stack
                right_operand = operand_stack.pop()
                left_operand = operand_stack.pop()
                
                # Apply the operator and push the result back to the stack
                result = operator_functions[token](left_operand, right_operand)
                operand_stack.append(result)
            else:  # If the token is a number
                operand_stack.append(int(token))
        
        # The final result will be the only element left in the stack
        return operand_stack.pop()
