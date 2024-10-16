class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={} # index and value

        for i, n in enumerate(nums):
            differnece = target-n
            if differnece in prevMap:
                return [prevMap[differnece],i]
            prevMap[n]=i
        