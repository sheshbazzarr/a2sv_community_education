class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        step_sum=0
        min_value = 0

        for num in nums:
            step_sum+=num
            min_value=min(min_value,step_sum)
        return 1-min_value
        

