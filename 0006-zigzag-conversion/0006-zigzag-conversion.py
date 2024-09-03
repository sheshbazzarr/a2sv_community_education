class Solution:
    def convert(self,s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        # Initialize an array of strings to represent each row
        rows = [''] * numRows
        cur_row = 0
        moving_down = True  # Initialize direction as moving downwards
        
        for chr in s:
            rows[cur_row] += chr
            
            # Determine if we need to change direction
            if cur_row == 0:
                # If we're at the top row, we should start moving downwards
                moving_down = True
            elif cur_row == numRows - 1:
                # If we're at the bottom row, we should start moving upwards
                moving_down = False
            
            # Move the current row pointer based on the direction
            if moving_down:
                cur_row += 1  # Move down to the next row
            else:
                cur_row -= 1  # Move up to the previous row

        # Combine all the rows to form the final converted string
        return ''.join(rows)