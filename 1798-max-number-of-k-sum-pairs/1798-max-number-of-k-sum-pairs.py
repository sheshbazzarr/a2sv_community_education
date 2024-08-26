class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        map_freqency=defaultdict(int)
        for num in nums:
            compliment = k-num
            if map_freqency[compliment] > 0:
                count+=1
                map_freqency[compliment]-=1

            else:
                map_freqency[num]+= 1
        return count
