class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #  the game is about finding smallest and second smallest number
        # infit
        first = second = float('inf')
        for num in nums:
            if num<=first:   # doest the first greater than the number
                first =num
            elif num<=second:
                second =num
            else:
                return True  # if there is a third then it is right 
        return False