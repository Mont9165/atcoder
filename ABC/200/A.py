a = int(input())

s = int(a / 100)

if s*100 < a:
    s += 1
    
print(s)

