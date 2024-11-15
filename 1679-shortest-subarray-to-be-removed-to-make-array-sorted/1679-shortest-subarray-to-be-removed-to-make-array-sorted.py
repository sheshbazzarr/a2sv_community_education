from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Step 1: Remove non-decreasing suffix
        arr_size = len(arr)
        right_bound = arr_size - 1
        while right_bound > 0 and arr[right_bound - 1] <= arr[right_bound]:
            right_bound -= 1

        # If the array is already sorted
        if right_bound == 0:
            return 0

        # Initialize the minimum length of subarray to remove
        min_length_to_remove = right_bound

        # Step 2: Remove non-decreasing prefix
        left_bound = 0
        while left_bound + 1 < arr_size and arr[left_bound] <= arr[left_bound + 1]:
            left_bound += 1

        min_length_to_remove = min(min_length_to_remove, arr_size - 1 - left_bound)

        # Step 3: Remove middle subarray
        left_pointer, right_pointer = 0, right_bound
        while left_pointer <= left_bound:
            # Find the valid position in the right subarray
            while right_pointer < arr_size and arr[left_pointer] > arr[right_pointer]:
                right_pointer += 1
            
            # Update the minimum length to remove
            min_length_to_remove = min(min_length_to_remove, right_pointer - left_pointer - 1)
            
            # Move the left pointer forward
            left_pointer += 1

        return min_length_to_remove
