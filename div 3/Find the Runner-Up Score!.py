if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    if len(arr) == 0:
        print(-1)
    else:
        a = max(arr)
        cou = arr.count(a)

        for i in range(cou):
            arr.remove(a)

        print(max(arr))
    
