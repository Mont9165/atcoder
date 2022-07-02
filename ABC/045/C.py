S = input()
n = len(S)-1
sum = 0

for i in range(2**n):
    num = 0
    for j in range(n+1):
        if ((i >> j) & 1):
            sum += int(S[num:j+1])
            num = j+1
    sum += int(S[num:])

print(sum)
