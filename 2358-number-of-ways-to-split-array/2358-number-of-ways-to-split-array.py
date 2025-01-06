class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        total_sum =sum(nums)
        cnt=0
        left_sum=0
        for i in nums[:-1]:
            left_sum=i+left_sum
            balance=total_sum-left_sum
            if left_sum>=balance:
                cnt+=1
        return cnt