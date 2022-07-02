n, k = map(int,input().split())
s = n*[0]
for i in range(n):
    s[i] = input()

alpha = 26
answer = 0

for i in range(2**n):
    count = alpha*[0]
    for j in range(n):
        if((i >> j) & 1):
            for letter in s[j]:
                count[ord(letter)-97] += 1
    answer = max(answer, count.count(k))

print(answer)