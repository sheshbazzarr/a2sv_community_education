class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i+1]
                nums[i+1]=0
        newarray=[]
        for num in nums:
            if num !=0:
                newarray.append(num)
        for num in nums:
            if num==0:
                newarray.append(num)
        return newarray
