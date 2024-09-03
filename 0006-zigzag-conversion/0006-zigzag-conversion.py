class Solution:
    def convert(self,s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=numRows:
            return s
        rows=['']*numRows
        cur_row=0
        can_I_go_down=False
        
        for chr in s:
            rows[cur_row]+=chr
            # you can change dir
            if cur_row ==0 or cur_row==numRows-1:
                can_I_go_down = not can_I_go_down
            cur_row+=1 if can_I_go_down else -1
        return ''.join(rows)
