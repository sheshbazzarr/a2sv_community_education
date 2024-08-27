class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find the rook's position
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook_row, rook_col = i, j
                    break

        # Initialize the count of attacked pawns
        attack_pawn = 0

        # Check right
        for i in range(rook_col + 1, 8):
            if board[rook_row][i] == "p":
                attack_pawn += 1
                break
            elif board[rook_row][i] == "B":
                break

        # Check left
        for i in range(rook_col - 1, -1, -1):
            if board[rook_row][i] == "p":
                attack_pawn += 1
                break
            elif board[rook_row][i] == "B":
                break

        # Check upward
        for j in range(rook_row - 1, -1, -1):
            if board[j][rook_col] == "p":
                attack_pawn += 1
                break
            elif board[j][rook_col] == "B":
                break

        # Check downward
        for j in range(rook_row + 1, 8):
            if board[j][rook_col] == "p":
                attack_pawn += 1
                break
            elif board[j][rook_col] == "B":
                break

        return attack_pawn
