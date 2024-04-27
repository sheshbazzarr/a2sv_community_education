# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read input
    n = int(input())
    a = list(map(int, input().split()))
    
    # Initialize variables
    operations = 0
    zeros_encountered = 0
    
    # Iterate through the array
    for i in range(n):
        # If the current element is zero
        if a[i] == 0:
            # Add the number of zeros encountered so far to operations
            operations += zeros_encountered
        # If the current element is one, update zeros_encountered
        else:
            zeros_encountered += 1
    
    # Output the minimum number of operations
    print(operations)
