import sys
n, k = map(int, sys.stdin.readline().split())
w = [0]*(n+1)
v = [0]*(n+1)
for i in range(1, n+1):
    w[i], v[i] = map(int, sys.stdin.readline().split())
dp = [[0 for i in range((k+1))] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if w[i] <= j:
            dp[i][j] = max(v[i] + dp[i-1][j-w[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])