N,K,Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in range(Q):
    if A[L[i]-1] != N:
        flag = False
        for j in range(K):
            if A[j] == (A[L[i]-1]+1):
                flag = True
                break
        if flag == False:
            A[L[i]-1] += 1
    #print(A)

print(*A)
