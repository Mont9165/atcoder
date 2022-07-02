n = int(input())
s, t = [], []

for i in range(n):
    S, T = input().split()
    s.append(S)
    t.append(int(T))

origin_num = -1
score = -1

judge = set()

for i in range(n):
    if s[i] not in judge:
        judge.add(s[i])
        if score < t[i]:
            origin_num = i
            score = t[i]

print(origin_num+1)