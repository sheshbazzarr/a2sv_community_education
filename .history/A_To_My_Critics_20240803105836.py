import sys
input = sys.stdin.read

data = input().strip().split()
t = int(data[0])

index = 1
for _ in range(t):
    num1 = int(data[index])
    num2 = int(data[index + 1])
    num3 = int(data[index + 2])
    index += 3

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
