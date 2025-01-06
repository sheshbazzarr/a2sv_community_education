class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        total_sum =sum(nums)   # time O(n)
        cnt=0
        left_sum=0
        for i in range(len(nums)-1):   #----> space O(n) creat an array and time ->O(n)
            left_sum+=nums[i]
            balance=total_sum-left_sum
            if left_sum>=balance:
                cnt+=1
        return cnt

        # space : O(n)
        # Time : O(n)