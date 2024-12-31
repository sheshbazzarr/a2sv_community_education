class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # Initialize the is_palindrome table
        is_palindrome = [[False] * n for _ in range(n)]
        # Initialize the cuts array
        cuts = [0] * n

        for i in range(n):
            min_cuts = i  # Maximum number of cuts is i (each character is a separate palindrome)
            for j in range(i + 1):
                # Check if s[j..i] is a palindrome
                if s[j] == s[i] and (i - j <= 1 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
                    # Update min_cuts
                    if j == 0:
                        min_cuts = 0  # No cut needed if the entire substring is a palindrome
                    else:
                        min_cuts = min(min_cuts, cuts[j - 1] + 1)
            cuts[i] = min_cuts

        return cuts[n - 1]