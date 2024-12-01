class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for f1 in range(len(nums)):
            for f2 in range(f1+1,len(nums)):
                if (nums[f1]+nums[f2])==target:
                    return [f1,f2]
        