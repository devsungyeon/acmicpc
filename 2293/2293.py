n, k = map(int, input().split())
li = []
for i in range(n):
    li.append(int(input()))

dp = [0]*(k+1)
for j in li:
    for i in range(j, k+1):
        if i == j:
            dp[i] = dp[i] + 1
        else:
            dp[i] = dp[i] + dp[i-j]
print(dp[k])