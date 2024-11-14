class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left ,right = 0,1
        result = 0
        while right<len(nums):
            diff=nums[right]-nums[left]
            if diff==1:
                result = max(result,right-left+1)
                right+=1
            elif diff<1:
                right+=1
            else:
                left+=1
            
            # if right==left:
            #     right+=1
            
        return result

# 0 1 2 2 2 2 3 3 5 7 