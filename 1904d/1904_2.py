#!/usr/bin/python3

n = int(input())
ans = [0]*2
ans[1] = 1
for i in range(n):
	ans[1] = int((ans[1] + ans[0])%15746)
	ans[0] = int((ans[1] - ans[0])%15746)
print(ans[1])
