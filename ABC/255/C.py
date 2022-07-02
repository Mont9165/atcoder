n, k = map(int, input().split())
a = list(map(int, input().split()))
 
a_sort = sorted(a)

for i in range(k):
    a[i:n:k] = sorted(a[i:n:k])
    
if a_sort == a:
    print("Yes")
else:
    print("No")