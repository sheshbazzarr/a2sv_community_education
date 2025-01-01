class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        # Initialize prefix_zeros and suffix_ones arrays
        prefix_zeros = [0] * (n + 1)
        suffix_ones = [0] * (n + 1)
        
        # Calculate prefix sum of zeros
        for i in range(1, n + 1):
            prefix_zeros[i] = prefix_zeros[i - 1] + (1 if s[i - 1] == '0' else 0)
        
        # Calculate suffix sum of ones
        for i in range(n - 1, -1, -1):
            suffix_ones[i] = suffix_ones[i + 1] + (1 if s[i] == '1' else 0)
        
        # Calculate the maximum score
        max_score = 0
        for i in range(1, n):  # Ensure both substrings are non-empty
            current_score = prefix_zeros[i] + suffix_ones[i]
            if current_score > max_score:
                max_score = current_score
        
        return max_score