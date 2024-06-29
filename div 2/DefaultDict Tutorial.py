# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
n,m = map(int,input().split())
for i in range(n):
    x = input()
    d[x].append(i+1)

for i in range(m):
    x = input()
    if x in d:
        print(*d[x])
    else:
        print('-1')
