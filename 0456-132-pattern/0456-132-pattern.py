class Solution:
    def find132pattern(self, nums):
        if len(nums)<3:
            return False
        stack = []
        second_number = float('-inf')

        for i in range(len(nums)-1,-1,-1):
            current_number = nums[i]

            if current_number<second_number:
                return True
            
            while stack and stack[-1]<current_number:
                second_number = stack.pop()
            stack.append(current_number)
        return False