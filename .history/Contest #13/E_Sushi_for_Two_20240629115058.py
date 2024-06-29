def longest_valid_segment(n, sushi):
    # Convert sushi types to a balance array where 1 -> +1 (tuna) and 2 -> -1 (eel)
    balance = [0] * n
    for i in range(n):
        if sushi[i] == 1:
            balance[i] = 1
        else:
            balance[i] = -1
    
    # Dictionary to store first occurrence of each balance value
    balance_map = {}
    balance_map[0] = -1  # Start with balance 0 at index -1 (before the array starts)
    
    max_length = 0
    current_balance = 0
    
    for i in range(n):
        current_balance += balance[i]
        
        if current_balance in balance_map:
            start_index = balance_map[current_balance]
            max_length = max(max_length, i - start_index)
        else:
            balance_map[current_balance] = i
    
    return max_length

# Reading input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
sushi = list(map(int, data[1:]))

# Calculate and print the result
print(longest_valid_segment(n, sushi))
