import sys


w = int(sys.stdin.readline().strip())

for each in range(w):
   
    lowercase = sys.stdin.readline().strip().lower()
    
    if lowercase == "yes":
        print("YES")
    else:
        print("NO")