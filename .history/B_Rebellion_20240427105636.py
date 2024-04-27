t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    operations = 0
    for i in range(n):
        operations += a[i:].count(0)
    print(operations)