def min_time(n, c, s):
    if c == 'g':
        return 0
    elif c == 'r':
        for i in range(n):
            if s[i] == 'g':
                return i + 1
    else:
        for i in range(n):
            if s[i] == 'g':
                return (i + 1) % n

t = int(input())
for _ in range(t):
    n = int(input())
    c, s = input().split()
    print(min_time(n, c, s))