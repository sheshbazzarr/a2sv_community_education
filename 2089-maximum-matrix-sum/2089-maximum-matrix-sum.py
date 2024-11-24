class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # what is the case so if i multiply the two elements 
        res = 0
        negative_count = 0
        matrix_min = float('inf')
        for row in matrix:
            for n in row:
                res+=abs(n)
                matrix_min =min(matrix_min,abs(n))
                if n<0:
                    negative_count+=1
        
        if negative_count & 1:
            res-=2*matrix_min
        return res