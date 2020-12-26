import sys
li = []
n = int(sys.stdin.readline())
for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort(key=lambda x: x[0])

li_b = []
dp = [0 for i in range(n)]
for i in li:
    li_b.append(i[1])
for i in range(n):
    for j in range(i):
        if li_b[i] > li_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))