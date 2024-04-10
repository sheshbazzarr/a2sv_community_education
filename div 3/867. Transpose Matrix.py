class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_length = len(matrix)
        col_length = len(matrix[0])
        
       
        transposed_matrix = [[0]*row_length for x in range( col_length)]
        
        for row in range(row_length):
            for col in range(len(matrix[row])):
                transposed_matrix[col][row] = matrix[row][col]
        
        return transposed_matrix
