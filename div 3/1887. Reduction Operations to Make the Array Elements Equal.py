class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Sort the list in descending order
        sort_ = sorted(nums, reverse=True)
        # Initialize the operation count
        count = 0 
        # Iterate through the sorted list and count operations
        for i in range(1, len(sort_)):
            if sort_[i] < sort_[i - 1]:
                count += i
        
        return count

        
