class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Finding the rook's position
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break

        # Initialize count of attacked pawns
        pawn_count = 0

        # Check upward direction
        for r in range(rook_row - 1, -1, -1):
            if board[r][rook_col] == 'p':
                pawn_count += 1
                break
            elif board[r][rook_col] == 'B':
                break

        # Check downward direction
        for r in range(rook_row + 1, 8):
            if board[r][rook_col] == 'p':
                pawn_count += 1
                break
            elif board[r][rook_col] == 'B':
                break

        # Check leftward direction
        for c in range(rook_col - 1, -1, -1):
            if board[rook_row][c] == 'p':
                pawn_count += 1
                break
            elif board[rook_row][c] == 'B':
                break

        # Check rightward direction
        for c in range(rook_col + 1, 8):
            if board[rook_row][c] == 'p':
                pawn_count += 1
                break
            elif board[rook_row][c] == 'B':
                break

        return pawn_count