class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        len_n = len(needle)
        len_h = len(haystack)
        
        for i in range(len_h-len_n+1):
            if haystack[i:i+len_n]==needle:
                return i         
                            
        return -1