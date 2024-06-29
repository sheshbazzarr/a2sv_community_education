import sys

input = sys.stdin.read

data = input().strip().split()
t = int(data[0])

result = []
index = 1
for i in range(1, t + 1):
    a = int(data[index])
    b = int(data[index + 1])
    index += 2
    
    maini = min(a, b)
    maxi = max(a, b)
    c = maxi // 4
    if c >  maini:
        result.append(maini)
    else:
        co = (maxi + maini) // 4
        result.append(co)

for ops in result:
    print(ops)
