class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq_map = defaultdict(int)
        
        # Count frequencies of each number
        for num in nums:
            freq_map[num] += 1

        count = 0
        
        for num in list(freq_map.keys()):  # Iterate over a copy of keys to avoid modifying the dictionary during iteration
            complement = k - num
            if complement in freq_map:
                if num == complement:
                    # Special case: num == complement (e.g., k = 6, num = 3)
                    count += freq_map[num] // 2
                else:
                    # Regular case: num != complement
                    pairs = min(freq_map[num], freq_map[complement])
                    count += pairs
                    freq_map[num] -= pairs
                    freq_map[complement] -= pairs
                    
        return count