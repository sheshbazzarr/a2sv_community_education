import sys
input = sys.stdin.read

data = input().strip().split()
t = int(data[0])

results = []
index = 1
for _ in range(t):
    a = int(data[index])
    b = int(data[index + 1])
    index += 2
    
    # Calculate maximum teams
    max_teams = min(a, b, (a + b) // 3)
    
    results.append(max_teams)

for result in results:
    print(result)
