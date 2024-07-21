class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        """ 
        the interesection of two array you will return the interesection between two array list you will return the same length of intereesection 
        first length and second length sum is more than 1 
        and on each array the start muust be greather than end of previous 
        and for each array the start is less than end 
        and end previious is less than start of next 
        compare the start of each array and the end of each corresponding array 
        then you will return the larger  of the start and the minimum of the end 
        [max(start1,start2),min(end1,end2)]
        it's takes on time becuase i should i trate over the whole list if i use poointer it would make it easier to .

        
        """
    
        if not secondList or not firstList:
            return [] 
        i=0
        j=0
        res=[]
        while i<len(firstList) and j<len(secondList):
            start1,end1=firstList[i]
            start2,end2=secondList[j]

            if start1>end2:
                j+=1
            elif start2>end1:
                i+=1
            else:
                res.append([max(start1,start2),min(end1,end2)])
                if end1>end2:
                    j+=1
                else:
                    i+=1
        return res

# july 21, 2024
