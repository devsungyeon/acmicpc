#!/usr/bin/python3

n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n):
	cnt = 0
	for j in range(i):
		if a[i] > a[j] and dp[i] < dp[j]:
			dp[i] = dp[j]
	dp[i] += 1
print(max(dp))



