class Solution:
    def rotate_90_clockwise(self, mat: List[List[int]]) -> None:
        n = len(mat)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        # Reverse each row
        for i in range(n):
            mat[i].reverse()

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Check if the matrices are initially equal
        if mat == target:
            return True
        
        # Rotate and check up to three more times
        for _ in range(3):
            self.rotate_90_clockwise(mat)
            if mat == target:
                return True
        
        # No match found after all possible rotations
        return False