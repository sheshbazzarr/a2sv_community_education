class Solution:
    def convert(self,s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of strings, one for each row
        rows = [''] * numRows
        cur_row = 0
        going_down = False

        for char in s:
            rows[cur_row] += char
            # Change direction when you reach the top or bottom row
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        # Combine all rows to form the final output
        return ''.join(rows)
