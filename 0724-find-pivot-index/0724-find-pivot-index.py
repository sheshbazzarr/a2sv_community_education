class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]
        total=prefix_sum
        left_sum = 0
        for i ,num in enumerate(nums):
            right_sum = total[-1]-left_sum -num
            if right_sum==left_sum:
                return i

            left_sum+=num
        return -1

        