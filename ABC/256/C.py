h1,h2,h3,w1,w2,w3 = map(int, input().split())
ans = 0
for a in range(1,29):
    for b in range(1,29):
        for d in range(1,29):
            for e in range(1,29):
                c = h1-a-b
                f = h2-d-e
                g = w1-a-d
                h = w2-b-e
                i_h = h3-g-h
                i_w = w3-c-f
                if min(c,f,g,h,i_h,i_h) > 0 and i_h == i_w:
                    ans += 1
print(ans)