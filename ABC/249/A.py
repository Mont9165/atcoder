a, b, c, d,e,f,x = map(int, input().split())

ta = int(x/(a+c))
ao = int(x/(d+f))

taka = 0
aoki = 0
if ta == 0:
    if x < a:
        taka += x*b
    else:
        taka += a*b
else:
    taka += ta*a*b
    if x-(ta*(a+c)) > a:
        taka += a*b
    else:
        taka += (x-(ta*(a+c)))*b

if ao == 0:
    if x < d:
        aoki += x*e
    else:
        aoki += d*e
else:
    aoki += ao*d*e
    if x-(ao*(d+f)) > d:
        aoki += d*e
    else:
        aoki += (x-(ao*(d+f)))*e

#print(taka)
#print(aoki)

if taka == aoki:
    print('Draw ')
elif taka < aoki:
    print('Aoki')
else:
    print('Takahashi')


