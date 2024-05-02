# Enter your code here. Read input from STDIN. Print output to STDOUT
A= set(map(int, input().split()))
n = int(input())
ans = True
for x in range(n):
    S = set(map(int, input().split()))
    if len(S) >= len(A):
        ans = False
        break
    for i in S:
        if i not in A:
            ans = False
            break
    if not ans: break
print(ans)
