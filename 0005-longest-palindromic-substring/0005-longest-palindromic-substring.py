class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes
            p1 = expand_around_center(i, i)
            # Even length palindromes
            p2 = expand_around_center(i, i + 1)
            # Update longest palindrome
            longest = max(longest, p1, p2, key=len)

        return longest