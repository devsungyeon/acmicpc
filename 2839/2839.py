#!/usr/bin/python3
import sys

n= int(input())

k = int(n/5)
m = n%5

while m%3 != 0:
	k = k-1
	m = m+5
	if k<0:
		print(-1)
		sys.exit()
print(int(k+m/3))
