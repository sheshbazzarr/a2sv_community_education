import sys

# Read the input value from the command line
w = sys.stdin.readline().strip()

# Convert the input to lowercase
lower = w.lower()

# Check if the input is "yes"
if lower == "yes":
    print("YES")
else:
    print("NO")