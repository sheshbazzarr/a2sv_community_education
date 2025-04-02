class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range (j+1,n):
                    res=max(res,(nums[i]-nums[j])*nums[k])
        return res 


        # b=a=float('-inf')
        

        # for i in range(len(nums)):
        #     if nums[i]>a:
        #         a=nums[i]
        #     elif nums[i]<a:
        #         b=nums[i]
        #     elif nums[i]>b:
                