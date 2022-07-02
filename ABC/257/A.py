n,x = map(int, input().split())

ans = int(x/n)
#print(ans)
if ans < x/n:
    print(chr(64+ans+1))    
else:
    print(chr(64+ans))

