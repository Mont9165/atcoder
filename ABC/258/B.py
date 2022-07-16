n = int(input())
A = []
for _ in range(n):
    A.append(input())
X = [[1,0], [-1,0], [0,1], [0,-1],[1,1], [1,-1], [-1,1], [-1,-1]]

ans = 0
for i in range(n):
    for j in range(n):
        for k in X:
            tmp = []
            x = i 
            y = j 
            for _ in range(n):                
                tmp.append(A[x][y])
                x += k[0] 
                y += k[1]
                x %= n
                y %= n
            ans = max(ans, int("".join(tmp)))
 
print(ans)  