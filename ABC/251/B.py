def judge(seisu, value):
    if value <= W:
        if value not in seisu:
            seisu.add(value)
 
N, W = map(int, input().split())
A = list(map(int, input().split()))
 
seisu = set()

for i in range(N):
    if A[i] <= W:
        judge(seisu, A[i])
        for j in range(i+1,N):
            if A[i]+A[j] <= W:
                judge(seisu, A[i]+A[j])
                for k in range(j+1, N):
                    judge(seisu, A[i]+A[j]+A[k])
 
 

print(len(seisu))
