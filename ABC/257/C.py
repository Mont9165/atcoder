N = int(input())
S = input()
W = list(map(int, input().split()))

adult, child = [], []

for i in range(N):
    if S[i] == '0':
        child.append(W[i])
    else:
        adult.append(W[i])
child.sort()
adult.sort()

