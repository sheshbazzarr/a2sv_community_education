class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t =s+s
        return s in t[1:-1]
      
