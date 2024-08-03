import sys
input = sys.stdin.read

# Read all input at once
data = input().strip().split()

# Index to track the current position in the input data
index = 0

# Number of test cases
t = int(data[index])
index += 1

results = []

for _ in range(t):
    # Length of the array
    n = int(data[index])
    index += 1
    
    # Array elements
    arr = list(map(int, data[index:index + n]))
    index += n
    
    # Calculate maximum possible sum (sum of absolute values)
    max_sum = sum(abs(x) for x in arr)
    
    # Calculate minimum number of operations
    operations = 0
    for num in arr:
        if num < 0:
            operations += 1

    results.append(f"{max_sum} {operations}")

# Print all results
print("\n".join(results))
