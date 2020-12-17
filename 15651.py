from itertools import product
n, m = map(int, input().split())
li = [i for i in range(1,n+1)]

def nondescending(li):
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            return False
    return True

for i in product(li, repeat=m):
    if nondescending(i):
        for j in i:
            print(j, end=' ')
        print()