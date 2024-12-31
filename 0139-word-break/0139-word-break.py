class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)  # Convert wordDict to a set for O(1) lookups
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string can always be segmented

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # No need to check further for this i

        return dp[n]