import sys
input = sys.stdin.read

data = input().strip().split()

index = 0
t = int(data[index])
index += 1

results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    arr = list(map(int, data[index:index + n]))
    index += n
    
    max_sum = sum(abs(x) for x in arr)
    operations = 0
    negative_segment = False

    for num in arr:
        if num > 0:
            negative_segment = False
        elif num < 0:
            if not negative_segment:
                operations += 1
            negative_segment = True

    results.append(f"{max_sum} {operations}")

print("\n".join(results))
