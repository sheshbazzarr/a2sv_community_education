class Solution:
    def removeDuplicates(self, s: str) -> str:
        j = 0
        s=list(s)
        for i in range(len(s)):
            # check if we have adjectnt duplicate
            if j>0 and s[j-1]==s[i]:
                j-=1
                # we don't place the chr at the j point
            else:
                s[j]=s[i]
                j+=1
        return ''.join(s[:j])
