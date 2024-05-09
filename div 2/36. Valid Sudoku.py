lass Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)  # Number of rows
        m = len(board[0])  # Number of columns

        # Check each row for duplicates
        for row in range(n):
            row_set = set()
            for col in range(m):
                if board[row][col] != '.':
                    if board[row][col] in row_set:
                        return False
                    row_set.add(board[row][col])

        # Check each column for duplicates
        for col in range(m):
            col_set = set()
            for row in range(n):
                if board[row][col] != '.':
                    if board[row][col] in col_set:
                        return False
                    col_set.add(board[row][col])

        # Check each 3x3 subgrid for duplicates
        for i in range(0, n, 3):
            for j in range(0, m, 3):
                subgrid_set = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        if board[row][col] != '.':
                            if board[row][col] in subgrid_set:
                                return False
                            subgrid_set.add(board[row][col])

        return True
