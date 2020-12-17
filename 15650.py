import itertools
n, m = map(int, input().split())
li = [i for i in range(1,n+1)]
perli = list(itertools.combinations(li,m))
for i in perli:
    for j in i:
        print(j, end=' ')
    print()