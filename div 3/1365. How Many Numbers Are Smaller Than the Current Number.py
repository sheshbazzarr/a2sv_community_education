class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 101):
            count[i] += count[i-1]
        count_list = []  
        for num in nums:  
            result = count[num]  
            count_list.append(result)  
        return count_list
