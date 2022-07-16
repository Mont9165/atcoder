n,q = map(int, input().split())
s = input()
p = 0
ans = []
for _ in range(q):
    t,x = map(int, input().split())
    if t == 1:
        p += x
    if t == 2:
        print(s[(x-1-p) % n])





