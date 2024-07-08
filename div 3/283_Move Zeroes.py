class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        resu = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                resu.append(0)
            else:
                i += 1
        return nums.extend(resu)
#july,8 2024
