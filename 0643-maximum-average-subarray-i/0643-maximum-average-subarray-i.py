class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Step 1: Calculate the sum of the first k elements.
        # This takes O(k) time since the sum function iterates over the first k elements.
        currSum = maxSum = sum(nums[:k])  # --> O(k)

        # Step 2: Iterate through the remaining elements in nums starting from index k.
        # The loop runs (n - k) times, where n is the length of the list nums.
        # The loop's time complexity is O(n - k), which simplifies to O(n).
        for i in range(k, len(nums)):  # --> O(n - k) --> O(n)
            
            # Step 3: Update the current sum by adding the new element nums[i] and
            # subtracting the element nums[i - k] that is sliding out of the window.
            # These are constant-time operations (O(1)).
            currSum += nums[i]          # --> O(1)
            currSum -= nums[i - k]      # --> O(1)

            # Step 4: Update maxSum to track the maximum sum encountered so far.
            # The max() function is a constant-time operation (O(1)).
            maxSum = max(maxSum, currSum)  # --> O(1)
        
        # Step 5: Return the maximum average by dividing maxSum by k.
        # This is a constant-time operation (O(1)).
        return maxSum / k  # --> O(1)

