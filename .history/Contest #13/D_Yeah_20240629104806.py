import sys


w = int(sys.stdin.readline().strip())

# Process each test case
for each in range(w):
   
    lowercase = sys.stdin.readline().strip().lower()
    
    if lowercase == "yes":
        print("YES")
    else:
        print("NO")