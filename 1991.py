import sys

n = int(sys.stdin.readline())
li = [[] for _ in range(n+1)]
for i in range(n):
    node, lchild, rchild = map(str, sys.stdin.readline().split())
    li[ord(node)-64] = [ord(lchild)-64, ord(rchild)-64]

def preorder(start, li):
    print(chr(start+64), end="")
    lchild = li[start][0]
    if lchild != -18:
        preorder(lchild, li)
    rchild = li[start][1]
    if rchild != -18:
        preorder(rchild, li)

def inorder(start, li):
    lchild = li[start][0]
    if lchild != -18:
        inorder(lchild, li)
    print(chr(start+64), end="")
    rchild = li[start][1]
    if rchild != -18:
        inorder(rchild, li)

def postorder(start, li):
    lchild = li[start][0]
    if lchild != -18:
        postorder(lchild, li)
    rchild = li[start][1]
    if rchild != -18:
        postorder(rchild, li)
    print(chr(start+64), end="")

preorder(1, li)
print()
inorder(1, li)
print()
postorder(1, li)