from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)  # O(1): Length of the code list.
        
        if k == 0:
            # O(n): Replace all elements with 0 in-place.
            for i in range(n):
                code[i] = 0
            return code
        
        original_code = code[:]  # O(n): Copy the original list for reference.
        
        if k > 0:
            # O(n * k): Outer loop runs n times, inner loop sums k elements.
            for i in range(n):
                code[i] = sum(original_code[(i + j) % n] for j in range(1, k + 1))
                # Inner loop computes sum of k elements using modulo for wrapping.
        else:  # k < 0
            # O(n * |k|): Similar to the above case but sums |k| elements in reverse.
            for i in range(n):
                code[i] = sum(original_code[(i + j) % n] for j in range(k, 0))
                # Inner loop computes sum of |k| elements.
        
        return code  # O(1): Return the modified code list.
