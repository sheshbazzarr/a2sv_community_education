class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # all it ask is . are there empty place which are not ajdecent that accomaodate n ?
        # check if there are not ? if is return True if not false
        # how we can check ?
        length=len(flowerbed)
        i=0
        while i <length and n>0:
            if flowerbed[i]==1:
                i+=2
            elif i==length-1 or flowerbed[i+1]==0:
                n-=1
                i+=2
            else:
                i+=3
        return n<=0