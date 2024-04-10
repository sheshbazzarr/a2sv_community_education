class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ROW_LE=len(grid)-2
        COL_LE=len(grid[0])-2
        ans=[[0]*ROW_LE  for x in range(COL_LE)]
        for row in range(ROW_LE):
            for col in range(COL_LE):
                ans[row][col]=grid[row][col]
                for row1 in range(3):
                    for col1 in range(3):
                        ans[row][col]=max(ans[row][col],grid[row+row1][col+col1])
        return ans
