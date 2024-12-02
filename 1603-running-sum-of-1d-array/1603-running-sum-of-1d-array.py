class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixsum = []
        current_sum =0
        for i,num in enumerate(nums):
            current_sum+=num
            prefixsum.append(current_sum)
        return prefixsum