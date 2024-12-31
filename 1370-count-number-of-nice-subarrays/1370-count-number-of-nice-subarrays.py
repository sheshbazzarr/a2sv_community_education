from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # Transform the array: 1 for odd, 0 for even
        transformed = [1 if num % 2 != 0 else 0 for num in nums]

        # Initialize prefix sum map
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1

        prefix_sum = 0
        result = 0

        for num in transformed:
            prefix_sum += num
            # If (prefix_sum - k) exists in the map, add its frequency to the result
            if (prefix_sum - k) in prefix_counts:
                result += prefix_counts[prefix_sum - k]
            # Update the prefix sum map
            prefix_counts[prefix_sum] += 1

        return result