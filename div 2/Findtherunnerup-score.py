if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))#cast the map object to list
    arr.sort(reverse=True)#sort in reverse order
    maxim=arr[0]#it is correct because the list is sorted in reverse order
    for i in arr:#what if there is a repetion for that case we itterat over the list 
        if i!=maxim:# 
            print(i)
            break