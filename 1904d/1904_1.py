#!/usr/bin/python3

n = int(input())
li = []
for i in range(1, n+1):
	if i==1: li.append(1)
	else:
		cnt = 0
		for j,val in enumerate(li):
			li[j] = int((li[j] * (i-cnt) / (i-2*cnt))%15736 )
			cnt = cnt+1
		if i%2 == 0:
			li.append(1)
ans = 0
for i in li:
	ans = int((ans + i)%15736)
print(ans)
