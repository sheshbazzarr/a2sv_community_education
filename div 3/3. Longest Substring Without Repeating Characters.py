class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() # hash table
        left = 0    #left slide
        max_length = 0  # lenght
        # still the time compleixty is o(n)
        for right in range(len(s)):# move the right slide
            while s[right] in char_set: # check if it is repeated 
                char_set.remove(s[left]) # then remove it from hashtable
                left += 1  # move left slide
            char_set.add(s[right])  # add right slide 
            max_length = max(max_length, right - left + 1)
        
        return max_length

        
