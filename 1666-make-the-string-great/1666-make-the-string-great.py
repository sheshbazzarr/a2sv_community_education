class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            found =0
            for i in range(len(s)-1):
                if s[i].swapcase()==s[i+1]:
                    s=s[:i]+s[i+2:]
                    found =1
                    break 
            if not found:
                break
        return s



        

    
