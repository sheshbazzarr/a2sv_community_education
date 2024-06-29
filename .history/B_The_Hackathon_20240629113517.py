import sys

input = sys.stdin.read

data = input().split()
t = int(data[0])

result=[]
for i in range(1,t+1):
      a, b = map(int, data[i].split())
    
    maini=min(a,b)
    maxi=max(a,b)
    c=maxi//4
    if maxi>maini:
        result.append(mani)
    else:
       co= (maxi+maini)//4
       print(co)

