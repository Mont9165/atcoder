def f(num):
    sum = 0
    while(num):
        sum += num % 10
        num //= 10
    return sum

n = int(input())
v = {}
for i in range(2*10**5):
    num = f(i)
    m = f(2*i)
    if num == n: v[i] = m

m = max(v.values())
x = 0
for i in v.items():
    #print(i[1])
    if i[1] == m:
        x = i[0]
        break

print(m)
print(x)


