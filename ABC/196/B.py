import math
x = input()
if '.' in x:
    x1, x2 = map(int, (x.split(".")))
    print(x1)
else:
    print(int(x))
