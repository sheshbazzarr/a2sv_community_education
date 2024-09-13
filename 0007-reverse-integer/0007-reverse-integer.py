class Solution:
    def reverse(self, x: int) -> int:
        MIN_VALUE = -2**31
        MAX_VALUE = 2**31 - 1
        
        # Determine the sign of the input number
        sign = -1 if x < 0 else 1
        x = abs(x)  # Work with the absolute value
        
        reversed_num = 0
        
        # Reverse the digits
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        reversed_num *= sign  # Apply the original sign back
        
        # Check for overflow
        if reversed_num < MIN_VALUE or reversed_num > MAX_VALUE:
            return 0
        else:
            return reversed_num