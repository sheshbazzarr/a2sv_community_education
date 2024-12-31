from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Initialize target_counts and required
        target_counts = defaultdict(int)
        for char in t:
            target_counts[char] += 1
        required = len(target_counts)

        # Initialize window_counts and formed
        window_counts = defaultdict(int)
        formed = 0

        # Initialize pointers and result
        left = 0
        min_length = float('inf')
        result = ""

        # Sliding window
        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1

            # Check if the current character matches the target frequency
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            # Contract the window
            while formed == required and left <= right:
                # Update the result if the current window is smaller
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    result = s[left:right + 1]

                # Move the left pointer
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1
                left += 1

        return result