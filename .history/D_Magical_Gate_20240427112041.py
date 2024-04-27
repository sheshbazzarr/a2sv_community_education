# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read input
    n, color = input().split()
    n = int(n)
    s = input().strip()
    
    # Find the index of the first occurrence of the green glow
    green_index = s.index('g')
    
    # Calculate the length of the string
    length = len(s)
    
    # Determine the distance between the current position and the next green glow
    if s[green_index] == color:
        # Green glow is the current color, so no waiting time needed
        print(0)
    elif green_index >= n // 2:
        # Current position is after or at the middle of the green glow cycle
        print(n - green_index)
    else:
        # Current position is before the middle of the green glow cycle
        print(green_index + 1)
