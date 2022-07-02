t = int(input())
case = []
length = []
for i in range(t):
    num = input()
    case.append(num)
    length.append(len(num))

ans = []

for i in range(t):
    if length[i] % 2 == 0:
        front = case[i][:length[i]//2]
        back = case[i][length[i]//2:]
        if front == back:
            tmp = front+back
            ans.append(int(tmp))
        elif front < back:
            tmp = front+front
            ans.append(int(tmp))
        else:
            next_front = str(int(front)-1)
            tmp = next_front+next_front
            ans.append(int(tmp))
    else:
        ans.append(pow(10, length[i]-12) -1 )

print(ans)