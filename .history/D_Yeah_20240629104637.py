import sys

# Read number of test cases
t = int(sys.stdin.readline().strip())

# Process each test case
for _ in range(t):
    # Read the string and convert to lowercase
    s = sys.stdin.readline().strip().lower()
    
    # Check if the string is "yes" and print the result
    if s == "yes":
        print("YES")
    else:
        print("NO")