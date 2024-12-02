class Solution:
    def maxScore(self, s: str) -> int:
        
        max_score = 0
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]
            left_zeros = left.count('0')
            right_ones = right.count('1')

            score = left_zeros+right_ones

            max_score = max(max_score,score)
        return max_score

        # Time complexity O(n^2)
        # space O(n)