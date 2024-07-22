class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_slide = 0
        max_length = 0
        zero_count = 0  # Keep track of the number of zeros in the window

        for right_slide in range(len(nums)):
            if nums[right_slide] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left_slide] == 0:
                    zero_count -= 1
                left_slide += 1

            max_length = max(max_length, right_slide - left_slide)

        return max_length
