import sys

input = sys.stdin.read

def minimal_crossing_time(n, current_color, s):
    # Find all occurrences of 'g' in the string s
    g_positions = []
    for i in range(n):
        if s[i] == 'g':
            g_positions.append(i)
    
    min_time = float('inf')
    
    # Calculate the time until the next 'g' for each found position
    for pos in g_positions:
        if s[pos] == 'g':
            if s[pos] == current_color:
                min_time = min(min_time, 0)
            else:
                # Calculate distance to the next 'g'
                for i in range(n):
                    if s[(pos + i) % n] == 'g':
                        min_time = min(min_time, i)
                        break
    
    return min_time

# Read input
data = input().splitlines()
t = int(data[0])

results = []
index = 1
for _ in range(t):
    n, current_color = data[index].split()
    n = int(n)
    s = data[index + 1]
    index += 2
    
    result = minimal_crossing_time(n, current_color, s)
    results.append(result)

# Print results
for result in results:
    print(result)
