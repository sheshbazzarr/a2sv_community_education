class Solution:
    def isCovered(self, ranges, left: int, right: int):
        inclusive=set()  
        for  i,j in ranges:
            for k in range(i,j+1):
                inclusive.add(k)    
        for i in range(left,right+1):
            if i not in inclusive:
                return False
            return True



        