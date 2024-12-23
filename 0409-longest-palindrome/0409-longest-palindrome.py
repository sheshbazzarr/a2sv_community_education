class Solution:
    def longestPalindrome(self, s: str) -> int:
   
         # Dictionary to store frequency of occurrence of each char
        frequency_map = {}
        for char in s:
            if char in frequency_map:
                frequency_map[char] += 1
            else:
                frequency_map[char] = 1  # Fixed: Initialize frequency when not present

        res = 0
        has_odd_frequency = False

        for count in frequency_map.values():
            if count % 2 == 0:
                res += count  # Add even frequencies directly
            else:
                res += count - 1  # Add the largest even part of odd counts
                has_odd_frequency = True  # At least one odd frequency exists

        # If there's an odd frequency, we can place one character in the middle of the palindrome
        return res + 1 if has_odd_frequency else res