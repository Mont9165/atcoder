s = input()

flag = False


string = list()

for i in s:
    string.append(i)

up = False
low = False
for i in range(len(string)):
    if string[i].isupper():
        up = True
    if string[i].islower():
        low = True
    if up and low:
        break

if up == False:
    print('No')
    exit()
if low == False:
    print('No')
    exit()

for i in range(len(string)):
    for j in range(i+1, len(string)):
        if string[i] == string[j]:
            print('No')
            exit()

print('Yes')