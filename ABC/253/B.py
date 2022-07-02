h, w = map(int, input().split())
s = []
koma = []
for i in range(h):
    s.append(input())
    for j in range(w):
        if s[i][j] == 'o':
            koma.append([i,j])
ans = abs(koma[0][0]-koma[1][0]) + abs(koma[0][1]-koma[1][1])
print(ans)