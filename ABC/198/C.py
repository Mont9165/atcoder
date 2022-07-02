
def main():
    n = int(input())
    s = list(input())
    q = int(input())
    flip = 0

    for _ in range(q):
        t,a,b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            a = (a+n*flip)%(2*n)
            b = (b+n*flip)%(2*n)
            s[a], s[b] = s[b], s[a]
        else:
            flip ^= 1

    if flip == 1:
        s = s[n:] + s[:n]
    print(''.join(s))

if __name__ == '__main__':
    main()