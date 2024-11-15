from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)  # O(1): Length of the list.
        result = [0] * n 
        if k == 0:
            return  result  # O(n): Return a list of zeros if k is 0.

        result = [0] * n  # O(n): Initialize the result list.
        
        
        start, end, step = (1, k + 1, 1) if k > 0 else (k, 0, 1)
        window_sum = sum(code[i % n] for i in range(start, end))  # O(k): Initialize the first window sum.

        for i in range(n):  # O(n): Slide the window across all positions.
            result[i] = window_sum  # Store the current window sum in the result.
            # Slide the window: Remove the outgoing element and add the incoming one.
            window_sum -= code[(i + start) % n]  # O(1): Remove outgoing element.
            window_sum += code[(i + end) % n]    # O(1): Add incoming element.
        
        return result  # O(1): Return the result list.
