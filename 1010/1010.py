import operator as op
from functools import reduce

def nCr(n, r):
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    if n == m:
        print(1)
    elif n > m:
        print(nCr(n,m))
    else:
        print(nCr(m,n))