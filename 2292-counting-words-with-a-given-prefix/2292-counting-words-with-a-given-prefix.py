class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count =0
        n=len(words)
        for i in range(n):
            if words[i].startswith(pref):
                count+=1
        return count