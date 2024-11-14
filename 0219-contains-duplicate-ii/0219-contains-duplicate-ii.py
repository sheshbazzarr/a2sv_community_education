class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windowset = set()
        L=0
        for R in range(len(nums)):
            if R-L>k:
                windowset.remove(nums[L])
                L+=1
            if nums[R] in windowset: #find the duplicate 
                return True 
            else:
                windowset.add(nums[R])

        return False