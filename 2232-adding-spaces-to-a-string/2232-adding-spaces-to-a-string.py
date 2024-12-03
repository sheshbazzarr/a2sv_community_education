class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Calculate the lengths of the spaces list and the string
        num_spaces, num_chars = len(spaces), len(s)
        
        # Create a result array of size num_spaces + num_chars filled with placeholders
        result_array = [' '] * (num_spaces + num_chars)
        
        space_pointer = 0  # Pointer to traverse the spaces list
        
        # Traverse through each character in the string
        for char_index, char in enumerate(s):
            # Check if we need to insert a space at the current position
            if space_pointer < num_spaces and char_index == spaces[space_pointer]:
                space_pointer += 1  # Move to the next space index
            
            # Insert the character into the result array, adjusted for spaces added so far
            result_array[char_index + space_pointer] = char
        
        # Join the result array into a single string and return
        return "".join(result_array)
