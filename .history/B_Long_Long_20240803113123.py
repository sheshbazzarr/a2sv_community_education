import sys
input = sys.stdin.read

def solve(test_cases):
    results = []
    for case in test_cases:
        n, arr = case
        max_sum = 0
        operations = 0
        negative_segment = False

        for num in arr:
            if num > 0:
                max_sum += num
                negative_segment = False
            elif num < 0:
                if not negative_segment:
                    operations += 1
                negative_segment = True
        
        results.append(f"{max_sum} {operations}")

    return results

# Reading input
data = input().strip().split()
t = int(data[0])

test_cases = []
index = 1
for _ in range(t):
    n = int(data[index])
    arr = list(map(int, data[index + 1:index + 1 + n]))
    test_cases.append((n, arr))
    index += n + 1

results = solve(test_cases)
print("\n".join(results))
