# Enter your code here. Read input from STDIN. Print output to STDOUT
int(input())
A = set(map(int,input().split()))
int(input())
B = set(map(int,input().split()))
res = A.union(B)

print(len(res))
