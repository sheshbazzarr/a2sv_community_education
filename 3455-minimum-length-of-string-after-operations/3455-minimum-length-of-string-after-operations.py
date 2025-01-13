class Solution:
    def minimumLength(self, s: str) -> int:
        n =len(s)
        count={}
        for i in range(n):
            if  s[i] not in count:
                count[s[i]]=1
            else:
                count[s[i]]+=1
        for char in count:
            while count[char]>2:
                count[char]-=2
        return sum(count.values())

        