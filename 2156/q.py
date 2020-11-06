#!/usr/bin/python3

n = int(input())

grape = [0]
dp = [0]

for i in range(1,n+1):
	grape.append(int(input()))
	if i==1:
		dp.append(grape[i])
	elif i==2:
		dp.append(grape[i]+grape[i-1])
	elif i==3:
		dp.append(max(dp[i-1],grape[1]+grape[3], grape[2] +grape[3]))
	else:
		dp.append(max(dp[i-1], dp[i-2]+grape[i], dp[i-3]+grape[i]+grape[i-1]))

print(dp[n])
		


