import sys

line = sys.stdin.readline().strip()
numbers = line.split(',')
num1, num2, num3 = list(map(int, numbers))

num1_max = max(num1, num2)
num2_max = max(num1, num3)
num3_max = max(num2, num3)

if num1 < 5 and num2 < 5 and num3 < 5:
    print("NO")
else:
    if num1_max + num2_max >= 10:
        print("YES")
    elif num1_max + num3_max >= 10:
        print("YES")
    elif num2_max + num3_max >= 10:
        print("YES")
    else:
        print("NO")
