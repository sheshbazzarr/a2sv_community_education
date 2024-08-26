class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        number_elements=len(matrix)
        # transpose
        for i in range(number_elements):
            for j in range (i+1,number_elements):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        # reverse the transpose row 
        for i in range(number_elements):
            left_ptr=0
            right_ptr=len(matrix[i])-1
            while left_ptr<right_ptr:
                matrix[i][left_ptr],matrix[i][right_ptr]=matrix[i][right_ptr], matrix[i][left_ptr]
                left_ptr+=1
                right_ptr-=1
        return matrix
