class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        garded_cell=[[0]*n  for _ in range(m) ]
        for r,c in walls:
            garded_cell[r][c]="W"
        for r,c in guards:
            garded_cell[r][c]="G"
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        # mark guarded cells 
        for row,col in guards:
            for dx,dy in direction:
                r=row+dx
                c=col+dy
                while 0 <= r< m and 0 <= c< n and garded_cell[r][c]!="W" and garded_cell[r][c]!="G" :
                    garded_cell[r][c]=1
                    r+=dx
                    c+=dy
        # count
        ungarded_cell=0
        for row in range(m):
            for col in range(n):
                if garded_cell[row][col]==0:
                    ungarded_cell+=1
        return ungarded_cell
