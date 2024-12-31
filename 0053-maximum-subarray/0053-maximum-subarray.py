class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize the variables
        max_sum = float('-inf')  # Start with the smallest possible number
        current_sum = 0
        
        # Iterate through the array
        for num in nums:
            current_sum += num  # Add the current number to the running sum
            max_sum = max(max_sum, current_sum)  # Update the max_sum if current_sum is larger
            if current_sum < 0:  # If current_sum becomes negative, reset it to 0
                current_sum = 0
        
        return max_sum