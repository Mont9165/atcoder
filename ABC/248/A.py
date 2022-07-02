s = int(input())

tmp = 0
while(True):
    a = s%10
    tmp += a
    s = (s-a)/10
    if s == 0:
        break

out = int(45-tmp)

print(out)

