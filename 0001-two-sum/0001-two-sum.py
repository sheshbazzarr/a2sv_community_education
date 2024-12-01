class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            y = target - num 
            if y in hash:
                return [hash[y], i]  
            hash[num] = i  
