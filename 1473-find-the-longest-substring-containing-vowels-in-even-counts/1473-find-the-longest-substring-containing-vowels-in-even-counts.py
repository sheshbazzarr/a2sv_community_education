class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Vowels and their corresponding bit positions 
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}  # '4' is now 4
        # Initialize bitmask and the dictionary to store the first occurrence of each bitmask
        bitmask = 0
        first_occurrence = {0: -1}
        max_length = 0

        for i, char in enumerate(s):
            # Update bitmask if the character is a vowel
            if char in vowels:
                bitmask ^= (1 << vowels[char])
            # If the bitmask is not in the dictionary, add it with the current index
            if bitmask not in first_occurrence:
                first_occurrence[bitmask] = i
            # Calculate the length of the substring with even vowels
            length = i - first_occurrence[bitmask]
            max_length = max(max_length, length)

        return max_length
