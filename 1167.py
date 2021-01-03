import sys
sys.setrecursionlimit(10 ** 9)
v = int(sys.stdin.readline())
tree = [[] for _ in range(v+1)]

for _ in range(v):
    li = list(map(int, sys.stdin.readline().split()))
    for i in range(1,len(li)-1,2):
        tree[li[0]].append([li[i], li[i+1]])

def DFS(start, tree, parents):
    for e,d in tree[start]:
        if parents[e] == 0:
            parents[e] = parents[start] + d
            DFS(e, tree, parents)

parents = [0 for _ in range(v+1)]
DFS(1, tree, parents)

index = parents.index(max(parents))
parents2 = [0 for _ in range(v+1)]
DFS(index, tree, parents2)
parents2[index] = 0
print(max(parents2))