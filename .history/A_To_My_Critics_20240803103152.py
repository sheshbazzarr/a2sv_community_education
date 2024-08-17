import sys
line=sys.stdin.readline().strip()
numbers=line.split(',')
num1,num2,num3=map(int,numbers)
num1_max=max(num1,num2)
num2_max=max(num2,num3)
num2_max=max(num1,num3)
if num1<5 and num2<5 and num3:
    print("NO")
else:
    if num1_max >5 and num2_max>5:
        print("YES")
    elif     