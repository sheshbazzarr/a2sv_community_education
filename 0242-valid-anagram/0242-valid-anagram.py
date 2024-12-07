class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_={}
        t_={}
        for i in s:
            if i not in s_:
                s_[i]=1
            s_[i]+=1
        for i in t:
            if i not in t_:
                t_[i]=1
            t_[i]+=1
        return True if s_==t_ else False
            