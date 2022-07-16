import math
a, b, c = map(int, input().split())
ad = a*math.cos(math.radians(c)) - b*math.sin(math.radians(c))
bd = a*math.sin(math.radians(c)) + b*math.cos(math.radians(c))
print(ad, ' ', bd)
