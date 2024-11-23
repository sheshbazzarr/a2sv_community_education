class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(","]":"[","}":"{"}
        for c in s:
            # if it is close 
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                # stack and closing curly brace check if they are equal .
                    stack.pop()
                else:
                    return False
            # else if it is open add it to stack
            else:
                stack.append(c)
        return True if not stack else False
            
