class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=j=0
        while i<len(t) and j < len(s):
            if s[j]==t[i]:
                j+=1
            i+=1
        if j>=len(s):
            return True
        else:
            return False 