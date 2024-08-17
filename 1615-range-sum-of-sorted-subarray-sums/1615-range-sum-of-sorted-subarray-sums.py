class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        val = []
        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                count += nums[j]
                val.append(count)
        mo=10**9+7
        val.sort()
        return sum(val[left-1 :right])%mo