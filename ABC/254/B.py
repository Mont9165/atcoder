N = int(input())

a = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(i+1):
        #print(a)
        if j == 0 or i == j:
            a[i][j] = 1
            print(a[i][j], end=" ")
        else:
            a[i][j] = a[i-1][j-1]+a[i-1][j]
            print(a[i][j], end=" ")
    print()