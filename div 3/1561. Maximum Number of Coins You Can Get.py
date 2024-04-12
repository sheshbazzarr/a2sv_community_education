class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        first_p = 0
        sec_p = len(piles) - 2
        sum = 0
        while first_p <= sec_p:
            sum += piles[sec_p]
            first_p += 1
            sec_p -= 2
        return sum
