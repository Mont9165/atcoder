from collections import defaultdict
import heapq

q = int(input())
s = defaultdict(int)
max_s = []
min_s = []
ans = []

for _ in range(q):
    query = [int(i) for i in input().split()]

    if query[0] == 1: 
        x = query[1]
        s[x] += 1
        heapq.heappush(max_s, -x)
        heapq.heappush(min_s, x)

    elif query[0] == 2: 
        x = query[1]
        c = query[2]
        s[x] -= min(c, s[x])
        if s[x] == 0:
            del s[x]
        
    elif query[0] == 3:
        while True:
            s_min = heapq.heappop(min_s)
            if s_min in s:
                heapq.heappush(min_s, s_min)
                break
        while True:
            s_max = -heapq.heappop(max_s)
            if s_max in s:
                heapq.heappush(max_s, -s_max)
                break
        ans.append(s_max-s_min)

for i in ans:
    print(i)