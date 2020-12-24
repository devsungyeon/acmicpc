import itertools
n,k = map(int, input().split())
print(len(list(itertools.combinations(range(n),k))))