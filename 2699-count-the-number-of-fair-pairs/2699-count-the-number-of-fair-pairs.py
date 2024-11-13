class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int: 
        nums.sort()
        total = 0
         
        for x in nums:
            low = bisect.bisect_left(nums,lower-x)
            hi =bisect.bisect_right(nums,upper-x)

            count = hi - low
            if lower-x <=x<=upper-x:
                count -=1
            total +=count
        return total//2
        
        