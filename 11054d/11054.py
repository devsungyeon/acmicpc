#!/usr/bin/python3
import sys
import operator

n = int(input())
li = list(map(int, input().split()))

inc = [1] * n
dec = [1] * n

for i in range(n):
	for j in range(i):
		if li[i] > li[j] and inc[i] <= inc[j]:
			inc[i] = inc[j] + 1

for i in range(n-1, -1, -1):
	for j in range(i,n):
		if li[i] > li[j] and dec[i] <= dec[j]:
			dec[i] = dec[j] + 1


print(  max(map(operator.add, inc, dec))-1)

