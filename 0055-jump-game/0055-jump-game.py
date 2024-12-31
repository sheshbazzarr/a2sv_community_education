class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0  # The farthest index we can reach
        
        # Iterate through the array
        for i in range(len(nums)):
            # If we are at an index that is beyond the farthest we can reach, return False
            if i > farthest:
                return False
            
            # Update the farthest index we can reach from the current position
            farthest = max(farthest, i + nums[i])
            
            # If we can reach or go beyond the last index, return True
            if farthest >= len(nums) - 1:
                return True
        
        # If we finish the loop and can't reach the last index, return False
        return False
