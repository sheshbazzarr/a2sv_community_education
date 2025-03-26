class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        return [sum(nums[:i+1]) for i in range(n)]