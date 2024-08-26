class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        number_elements=len(matrix)
        # transpose
        for i in range(number_elements):
            for j in range (i+1,number_elements):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        # reverse the transpose row 
        for i in range(number_elements):
            matrix[i].reverse()
            