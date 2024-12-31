from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize=None)  # Memoization decorator
        def dfs(s1: str, s2: str) -> bool:
            # Base cases
            if s1 == s2:
                return True
            if len(s1) != len(s2) or sorted(s1) != sorted(s2):
                return False

            # Try all possible splits
            n = len(s1)
            for i in range(1, n):
                # Case 1: No swap
                if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
                    return True
                # Case 2: Swap
                if dfs(s1[:i], s2[n - i:]) and dfs(s1[i:], s2[:n - i]):
                    return True

            return False

        return dfs(s1, s2)