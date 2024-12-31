class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):  # We don't need to jump from the last index
            farthest = max(farthest, i + nums[i])  # Update the farthest reachable index
            
            # If we have reached the end of the current jump range
            if i == current_end:
                jumps += 1  # Increment the number of jumps
                current_end = farthest  # Update the current end to the farthest reachable index
                
                if current_end >= n - 1:  # If we can reach or exceed the last index
                    break
        
        return jumps