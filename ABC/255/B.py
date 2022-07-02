N, K = map(int, input().split())

A = list(map(int, input().split()))


X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

dist = [[0 for _ in range(N)] for _ in range(N)]

ans = []
for j in range(N):
    dis = []
    for i in A:
        dist[i-1][j] = (((X[i-1]-X[j])**2) + ((Y[i-1]-Y[j])**2))**0.5
        dis.append(dist[i-1][j])
    ans.append(min(dis))

print(max(ans))