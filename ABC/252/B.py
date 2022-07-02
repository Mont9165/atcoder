def judge(seisu, value):
    if value <= W:
        if value not in seisu:
            seisu.add(value)
 
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max = list()
big = -1
for i in range(N):
    for j in range(N):
        if big < A[j]:
            big = A[j]
    if big == A[i]:
        max.append(i)

flag = False
for i in range(K):
    for j in range(len(max)):
        if B[i] == (max[j]+1):
            flag = True
            break

if flag:
    print('Yes')
else:
    print('No')
