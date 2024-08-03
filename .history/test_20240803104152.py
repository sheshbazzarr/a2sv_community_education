import sys
if len(sys.argv)!=4:
    print("usage: script.py num1 ,num2,num3")
    sys.exit(1)

line=sys.argv[1]
numbers=line.split(',')   