class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left_ptr=0
        right_ptr=len(nums)-1
        operation_count=0
        while left_ptr<right_ptr:
            current_sum=nums[left_ptr]+nums[right_ptr]
            if current_sum==k:
                operation_count+=1
                left_ptr+=1
                right_ptr-=1
            elif current_sum<k:
                left_ptr+=1
            else:
                right_ptr-=1
        return operation_count
