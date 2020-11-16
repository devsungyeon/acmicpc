n = int(input())
lst = list(map(int, input().split()))

p = [0]*1001
dp = [0]*1001

for i in range(1, n+1):
    p[i] = lst[i-1]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + p[j])
print(dp[n])