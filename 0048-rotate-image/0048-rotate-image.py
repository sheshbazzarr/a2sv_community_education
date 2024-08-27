class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    #    transpose and reverse it 
        size=len(matrix)
        for i in range(size):
            for j in range(i+1,size):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for i in range(size):
            matrix[i].reverse()
        