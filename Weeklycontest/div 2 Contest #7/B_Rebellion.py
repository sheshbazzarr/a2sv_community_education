t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    operations = 0
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            operations += a[i-1] - a[i]
            a[i] = a[i-1]
    print(operations)