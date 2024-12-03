from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Compute the lengths of the string and the spaces list
        num_chars,num_spaces = len(s),len(spaces)
        
        # Create an array of size num_chars + num_spaces to hold the result
        result_array = [''] * (num_chars + num_spaces)
        
        # Use two pointers: `char_index` for the string `s` and `space_index` for the spaces list
        char_index = 0
        space_index = 0
        
        # Iterate through the characters of `s`
        for i in range(num_chars):
            # If the current index matches the next space position, insert a space
            if space_index < num_spaces and char_index == spaces[space_index]:
                result_array[i + space_index] = ' '  # Place space at the correct position
                space_index += 1  # Move to the next space index
            
            # Add the current character of `s` to the result array
            result_array[i + space_index] = s[char_index]
            char_index += 1  # Move to the next character in `s`
        
        # Join the array to form the final string and return
        return ''.join(result_array)
