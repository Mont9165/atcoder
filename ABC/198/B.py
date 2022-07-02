n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

big = int(-5)
small = int(10000)

for i in range(n):
    if big < a[i]:
        big = a[i]
    if small > b[i]:
        small = b[i]

ans = int(0)

if big <= small:
    ans = small - big + 1
    print(ans)
else:
    print(ans)
