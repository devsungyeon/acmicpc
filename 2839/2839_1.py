#!/usr/bin/python3
n = int(input())
ans = 9999999999
for i in range(int(n/5)+1):
	if (n - i*5) % 3 == 0:
		ans = min(ans, (i+(n-i*5)/3))
if ans == 9999999999:	print(-1)
else:	print(int(ans))

