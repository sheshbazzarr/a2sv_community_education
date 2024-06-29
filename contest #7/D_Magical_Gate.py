t = int(input())
for _ in range(t):
    n = int(input())
    c, s = input().split()
    if c == 'g':
        print(0)
    elif c == 'r':
        for i in range(n):
            if s[i] == 'g':
                print(i + 1)
                break
    else:
        for i in range(n):
            if s[i] == 'g':
                print((i + 1) % n)
                break