class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target)!=len(arr):
            return False
        sett1={}
        sett2={}
        for x in target:
            if x not in sett1:
                sett1[x]=1
            sett1[x]+=1
        for y in arr:
            if y not in sett2:
                sett2[y]=1
            sett2[y]+=1

        return sett1==sett2