class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #  find the maximu on the array 
        #  then iterator for each value adding the extacandies 
        #  compare the maxim with those value and append either false or true
            #  if it is greater or equal  True 
            #  else False 
        # first is find the meximum of the array 
        maxs=max(candies)
        candiBool=[]
        for i in candies:
            if i+extraCandies>=maxs:
                candiBool.append(True)
            else:
                candiBool.append(False)

        return candiBool


