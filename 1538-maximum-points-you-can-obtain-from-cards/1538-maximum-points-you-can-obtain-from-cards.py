class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        # Sum of the first k cards
        window_sum = sum(cardPoints[:k])
        max_sum = window_sum

        # Slide the window from left to right
        for i in range(k - 1, -1, -1):
            window_sum -= cardPoints[i]  # Remove the i-th card from the beginning
            window_sum += cardPoints[n - k + i]  # Add the (n - k + i)-th card from the end
            max_sum = max(max_sum, window_sum)

        return max_sum