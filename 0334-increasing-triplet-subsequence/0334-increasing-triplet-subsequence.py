class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
    #    initailze two variables with very large value
        first = second = float('inf')

        for num in nums:
            if num <=first:
                first=num
            elif num <=second :
                second = num
            else:
                return True
        return False