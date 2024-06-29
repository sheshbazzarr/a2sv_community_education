import sys

input = sys.stdin.read

data = input().split()
t = int(data[0])
index = 1

results = []
for _ in range(t):
    a = int(data[index])
    b = int(data[index + 1])
    index += 2
    
    # Calculate maximum number of teams
    teams_3m = min(a, b)
    
    
    max_teams = teams_with_1p_3m + teams_with_3p_1m
    
    results.append(max_teams)

# Print all results
for result in results:
    print(result)
