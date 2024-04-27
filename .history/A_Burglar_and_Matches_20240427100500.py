while True:
    try:
        Box, n = map(int, input().split())
        M = []
        for _ in range(n):
            M.append(tuple(map(int, input().split())))
        
        M.sort(reverse=True)
        
        for m in M:
            print(m[0], m[1])

        ans = 0
        for i in range(n):
            if M[i][0] <= Box:
                ans += M[i][0] * M[i][1]
                Box -= M[i][0]
            else:
                ans += Box * M[i][1]
                Box = 0
            if Box <= 0:
                break

        print(ans)
    except EOFError:
        break
