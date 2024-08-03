import sys
if len(sys.argv)!=4:
    print("usage: script.py num1 ,num2,num3")
    sys.exit(1)

line=sys.argv[1]
numbers=line.split(',') 
num1=map(int,numbers)
print("number1",num1)
# print("number2",num2)
# print("number3",num3)

