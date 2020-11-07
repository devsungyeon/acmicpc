#!/usr/bin/python3
import operator as op
from functools import reduce
def ncr(n, r):
	r = min(r, n-r)
	numer = reduce(op.mul, range(n, n-r, -1), 1)
	denom = reduce(op.mul, range(1, r+1), 1)
	return numer//denom

n = int(input())
ans = 0
for i in range(n//2+1):
	ans = ans+ncr(n-i,i)
	ans = ans % 15746
print(ans)
