class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """ 
           this question is aking me to find sum of 3 distinct int in array which will result closest to targe.
           the constraint is the target is between -10k to 10k 
           and the array must be greater than or equal to 3 to 500 
           
           the output is :an integer ,closest to target .yet it 
           the implmentation will be done using two pointers .
           i don't know it order matter or not ,but i guess it does't matter 
           
           i will focus on : how many times i will add three integer 
            then i will compare among the result and return the closest to the target it could be the larges, among them ,middle or least yet it should be cloesest so there must me some howe i should implemnt that ,like trucking the differnce between target and the smallest 
            i will use python as my implementation programming language
        """
        nums.sort()  # Sort the array to use the two-pointer approach
        closest_sum = float('inf')  # Initialize closest sum to infinity
        
        for i in range(len(nums) - 2):  # Iterate through the array
            left, right = i + 1, len(nums) - 1  # Two pointers
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]  # Sum of the triplet
                if abs(current_sum - target) < abs(closest_sum - target):  # Check if it's closer
                    closest_sum = current_sum
                
                if current_sum < target:  # Move the left pointer to increase the sum
                    left += 1
                elif current_sum > target:  # Move the right pointer to decrease the sum
                    right -= 1
                else:  # If the current sum is exactly the target, return it
                    return current_sum
        
        return closest_sum  # Return the closest sum found
