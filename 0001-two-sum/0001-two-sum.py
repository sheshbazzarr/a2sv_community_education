class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        StoreHash={} # value and index
        for index ,value in enumerate(nums):
            difference=target-value
            if difference in StoreHash:
                return [StoreHash[difference],index]
            StoreHash[value]=index
       
      