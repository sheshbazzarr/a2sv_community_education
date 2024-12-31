class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)  # Convert wordDict to a set for O(1) lookups

        # Memoization to store results of subproblems
        memo = {}

        def backtrack(s: str) -> list[str]:
            if s in memo:
                return memo[s]

            if not s:
                return [""]  # Base case: empty string

            result = []
            for i in range(1, len(s) + 1):
                word = s[:i]
                if word in wordSet:
                    # Recursively segment the remaining substring
                    for sentence in backtrack(s[i:]):
                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)

            memo[s] = result
            return result

        return backtrack(s)