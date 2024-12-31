class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        left = 0
        max_sum = 0
        current_sum = 0
        unique_elements = set()

        for right in range(len(nums)):
            # If the current element is already in the window, move the left pointer
            while nums[right] in unique_elements:
                unique_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # Add the current element to the window
            unique_elements.add(nums[right])
            current_sum += nums[right]

            # Update the maximum sum
            max_sum = max(max_sum, current_sum)

        return max_sum