r, c = map(int, input().split())
a11, a12 = map(int, input().split())
a21, a22 = map(int, input().split())

if r == 1 and c == 1:
    print(a11)
elif r == 1 and c == 2:
    print(a12)
elif r == 2 and c == 1:
    print(a21)
else:
    print(a22)