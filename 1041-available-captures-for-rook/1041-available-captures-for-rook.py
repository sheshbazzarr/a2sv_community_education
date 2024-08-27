from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Step 1: Find the Rook's position
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break
            else:
                continue
            break
        
        # Define the four possible directions: right, down, up, left
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        attack_pawn = 0

        # Step 2: Check all four directions
        for dr, dc in directions:
            r, c = rook_row, rook_col
            while 0 <= r + dr < 8 and 0 <= c + dc < 8:
                r += dr
                c += dc
                if board[r][c] == 'p':
                    attack_pawn += 1
                    break
                elif board[r][c] == 'B':
                    break
        
        return attack_pawn
