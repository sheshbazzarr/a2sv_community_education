class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the input list in ascending order
        result = {}
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            
            left_p = i + 1
            right_p = len(nums) - 1
            
            while left_p < right_p:
                total_sum = nums[i] + nums[left_p] + nums[right_p]
                
                if total_sum == 0:
                    result[(nums[i], nums[left_p], nums[right_p])] = 1
                    # Move both pointers to avoid duplicates
                    left_p += 1
                    right_p -= 1
                    while left_p < right_p and nums[left_p] == nums[left_p - 1]:
                        left_p += 1
                    while left_p < right_p and nums[right_p] == nums[right_p + 1]:
                        right_p -= 1
                elif total_sum < 0:
                    left_p += 1
                else:
                    right_p -= 1
        
        return list(result.keys())
