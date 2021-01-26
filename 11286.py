import sys

def minheap(li, idx):
    if idx == 0:
        return
    if abs(li[idx]) < abs(li[(idx - 1) // 2]):
        li[idx], li[(idx - 1) // 2] = li[(idx - 1) // 2], li[idx]
        idx = (idx - 1) // 2
        minheap(li, idx)
    elif abs(li[idx]) == abs(li[(idx - 1) // 2]):
        if li[idx] < li[(idx - 1) // 2]:
            li[idx], li[(idx - 1) // 2] = li[(idx - 1) // 2], li[idx]    
            idx = (idx - 1) // 2
            minheap(li, idx)
        else:
            return
    else:
        return

def delminheap(li, idx):
    lc = (idx + 1)*2-1
    rc = (idx + 1)*2
    if lc < len(li):
        if rc < len(li): # lChild and rChild
            
        else: # only lChild
            
    else:
        return

n = int(sys.stdin.readline())
li = []
ans = []
for _ in range(n):
    tmp = int(sys.stdin.readline())
    
    if tmp != 0:
        li.append(tmp)
        minheap(li, len(li)-1)
    else:
        if not li:
            ans.append(0)
        else:
            ans.append(li[0])
            li[0], li[-1] = li[-1], li[0]
            del(li[-1])
            delminheap(li, 0)
print(ans)