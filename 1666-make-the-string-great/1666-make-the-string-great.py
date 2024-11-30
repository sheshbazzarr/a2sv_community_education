class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        while i< len(s):
            char = s[i]
            if stack:
                if char.isupper() and stack[-1].islower() and char.lower() == stack[-1]:
                    stack.pop()
                    i+=1
                    continue
                elif char.islower() and stack[-1].isupper() and char.upper()==stack[-1]:
                    stack.pop()
                    i+=1
                    continue
            
            stack.append(char)
            i+=1
        return ''.join(stack)
    
