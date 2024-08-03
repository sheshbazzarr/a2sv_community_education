import sys
input = sys.stdin.read

data = input().split()
t = int(data[0])
index = 1

results = []

for _ in range(t):
    a = int(data[index])
    b = int(data[index + 1])
    c = int(data[index + 2])
    index += 3
    
    if a + b >= 10 or a + c >= 10 or b + c >= 10:
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result)
