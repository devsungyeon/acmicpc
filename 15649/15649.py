from itertools import permutations
n, m = map(int, input().split())
a = list(x for x in range(1,n+1))
perm = list(permutations(a,m))
for i in perm:
    for j in i:
        print(str(j)+' ',end='')
    print()