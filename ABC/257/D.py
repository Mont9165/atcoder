n = int(input())
query = []

for i in range(n):
    l_t, r_t = map(int, input().split())
    query.append((l_t,0))
    query.append((r_t,1))

query.sort()
ans = 0
for time, flag in query:
    if(flag==0):
        if(ans==0):
            print(time, end=' ')
        ans += 1
    
    if(flag==1):
        ans -= 1
        if(ans==0):
            print(time)