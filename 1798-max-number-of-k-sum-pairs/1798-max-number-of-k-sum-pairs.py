class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        count = 0
        freq = defaultdict(int)  # A dictionary to store the frequency of each element
        
        for num in nums:
            complement = k - num
            if freq[complement] > 0:
                count += 1
                freq[complement] -= 1  # Use the complement, so decrease its count
            else:
                freq[num] += 1  # Otherwise, store the frequency of the current number
        
        return count