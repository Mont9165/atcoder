N = int(input())
S = []
for i in range(N):
    S.append(input())

count = [[0 for j in range(10)]for i in range(10)]

for i in range(N):
    for j in range(10):
        count[int(S[i][j])][j] += 1

time = [0 for i in range(10)]

for i in range(10):
    for j in range(10):
        time[i] = max(time[i], 10*(count[i][j]-1) + j)

print(min(time))