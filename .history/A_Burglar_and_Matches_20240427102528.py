n, m = map(int, input().split())
pa = []
for i in range(m):
    x, y = map(int, input().split())
    pa.append((x, y))

pa.sort(key=lambda x: x[1], reverse=True)

sum = 0
got = n
for x, y in pa:
    if x <= got:
        sum += x * y
        got -= x
    else:
        sum += got * y
        got -= got
        break

print(sum)