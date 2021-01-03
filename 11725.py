import sys
sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s,e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)
parents = [0 for _ in range(n+1)]

def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i, tree, parents)

DFS(1, tree, parents)

for i in range(2,n+1):
    print(parents[i])