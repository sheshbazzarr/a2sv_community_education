class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        perimeter=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]==0:# top
                        perimeter+=1
                    if i==row-1 or grid[i+1][j]==0: # bottom
                        perimeter+=1
                    if j==col-1 or grid[i][j+1]==0:# right
                        perimeter+=1
                    if j==0  or grid[i][j-1]==0: # left
                        perimeter+=1
        return perimeter