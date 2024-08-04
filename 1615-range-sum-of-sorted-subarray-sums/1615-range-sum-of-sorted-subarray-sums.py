class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        subarray_sums = []

        # Compute all subarray sums
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)

        # Sort the subarray sums
        subarray_sums.sort()

        # Compute the sum of elements from index left to right (1-based)
        MOD = 10**9 + 7
        result = sum(subarray_sums[left-1:right]) % MOD

        return result