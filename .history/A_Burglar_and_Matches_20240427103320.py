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

burglaries_num, matches_num = map(int, input().split())
burglaries_list = []
for i in range( matches_num):
    burglary_time, matches_needed = map(int, input().split())
    burglaries_list.append((burglary_time, matches_needed))

burglaries_list.sort(key=lambda x: x[1], reverse=True)

total_matches = 0
burglary_time_left = burglaries_num
for burglary_time, matches_needed  in burglaries_list:
    if burglary_time <= burglary_time_left:
        total_matches += burglary_time*matches_needed 
        burglary_time_left -=burglary_time
    else:
        total_matches += burglary_time_left * matches_needed
        burglary_time_left -= burglary_time_left
        break

print(total_matches)