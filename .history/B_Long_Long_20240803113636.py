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
    
    max_sum = 0
    operations = 0
    negative_segment = False

    for num in arr:
        if num > 0:
            max_sum += num
            negative_segment = False
        elif num < 0:
            if not negative_segment:
                operations += 1
            negative_segment = True

    results.append(f"{max_sum} {operations}")

# Print all results
print("\n".join(results))
