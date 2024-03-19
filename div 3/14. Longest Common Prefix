class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ''
        
        
        for i in range(len(strs[0])):
            letter = strs[0][i]
            
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != letter:
                    return longestPrefix
                
            longestPrefix+=letter
                
                
        
        return longestPrefix
