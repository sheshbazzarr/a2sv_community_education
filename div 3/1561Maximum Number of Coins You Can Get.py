class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum=0
        while piles:
            A=piles.pop()
            M=piles.pop()
            F=piles.pop(0)
            sum+=M
        return sum


july 7,2024
