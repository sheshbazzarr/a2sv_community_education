class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count=0
        sets={}
        for item in arr:
            if item in sets:
                sets[item]=False # not distinct
            else:
                sets[item]=True  # it is distinct
        # find the k-th distinct element
        for item in arr:
            if sets[item]:
                count+=1
                if count==k:
                    return item
        return ""