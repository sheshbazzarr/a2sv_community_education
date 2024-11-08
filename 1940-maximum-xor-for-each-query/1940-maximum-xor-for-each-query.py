from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_value = (1 << maximumBit) - 1  # This is the largest k we can use given maximumBit.
        currentXor = 0  # Start with no XOR

        # Compute the XOR of the entire array
        for num in nums:
            currentXor ^= num

        result = []

        # Iterate from the end of nums to the start
        for num in reversed(nums):
            k = max_value ^ currentXor  # This maximizes the XOR with currentXor
            result.append(k)  # Store the result for this "query"
            
            # Update currentXor by removing the last element
            currentXor ^= num

        return result
