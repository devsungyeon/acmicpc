import sys

n = int(sys.stdin.readline())
li = [[] for _ in range(n+1)]
for i in range(n):
    node, lchild, rchild = map(str, sys.stdin.readline().split())
    li[ord(node)-64] = [ord(lchild)-64, ord(rchild)-64]
    # . -__package__
print(li)
def preorder(start, li):
    print(chr(start), end="")
    lchild = li[start][0]
    rchild = li[start][1]
    if lchild != -18:
        preorder(lchild, li)
    if rchild != -18:
        preorder(rchild, li)
def inorder():
    return
def postorder():
    return

preorder(1, li)