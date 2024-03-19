class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for num in range(len(nums)):
            nums.append(nums[num])
        return nums
