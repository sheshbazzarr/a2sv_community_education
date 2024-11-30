class Solution:
    def find132pattern(self, nums):
        # Start by checking if the list has fewer than 3 elements
        if len(nums) < 3:
            # Can't have a 132 pattern with less than 3 numbers
            return False

        # Initialize a stack to keep track of potential nums[j] values
        stack = []

        # This variable will keep track of the second number in the 132 pattern (nums[k])
        second_number = float('-inf')  # Very small value, smaller than any number in the array

        # We need to iterate through the list backward
        for i in range(len(nums) - 1, -1, -1):
            current_number = nums[i]

            # Check if the current number is less than the second_number (nums[k])
            if current_number < second_number:
                # If true, we found the 132 pattern
                return True

            # Otherwise, we start updating the stack and second_number
            # While there are numbers in the stack and the top of the stack is smaller than the current number
            while stack and stack[-1] < current_number:
                # Pop from the stack and set it as the second_number
                second_number = stack.pop()

            # Push the current number onto the stack as a potential nums[j]
            stack.append(current_number)

        # If we finish the loop and don't find a pattern, return False
        return False
