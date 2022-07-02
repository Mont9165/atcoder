N = int(input())
A = list(map(int, input().split()))
x = [0]*N
p = 0
for i in range(N):
    for j in range(i+1):
        x[j] += A[i]
        if x[j] >= 4:
            p += 1
            x[j] = -float('inf')
#print(x)
print(p)
