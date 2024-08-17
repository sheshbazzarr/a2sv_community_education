import sys
input = sys.stdin.read

data = input().strip().split()
index = 0

t = int(data[index])
index += 1

results = []

for _ in range(t):
    x_coords = []
    y_coords = []
    
    for _ in range(4):
        x, y = int(data[index]), int(data[index + 1])
        x_coords.append(x)
        y_coords.append(y)
        index += 2
    
    # Calculate side length
    side_length = max(max(x_coords) - min(x_coords), max(y_coords) - min(y_coords))
    
    # Calculate area
    area = side_length * side_length
    results.append(str(area))

print("\n".join(results))
