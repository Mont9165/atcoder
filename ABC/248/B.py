a, b, k = map(int, input().split())

if b/a <= 1:
    print(0)
    exit()

b /= a
count = 1
while(True):
    
    if b/k <= 1:
        break
    b /= k
    count += 1

print(int(count))