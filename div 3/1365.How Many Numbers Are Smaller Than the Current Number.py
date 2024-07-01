class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = nums[:]
        result.sort()
        index = {}
        for i in range(len(result)):
            if result[i] not in index:
                index[result[i]] = i
        
        for i in range(len(nums)):
            result[i] = index[nums[i]]
        
        return result
