n, m, k = map(int, input().split())
mod = 998244353

dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1

for a in range(n):
    for b in range(k):
        for c in range(1, m+1):
            if b+c <= k:
                dp[a+1][b+c] += dp[a][b] % mod

ans = 0

for i in range(1, k+1):
    ans += dp[n][i] % mod

print(ans%mod)
