import operator as op
from functools import reduce
def nCr(n, r):
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator
n = int(input())
print(nCr(n+9,n)%10007)