if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # three loop 
    result = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:
                    result.append([i, j, k])
    
    # Printing the result
    print(result)

# this is a list comrhensions
result[[i,j,k]for i in range(x+1) for j in range(y+1)for k in range(z+1) if i+j+k!=n]