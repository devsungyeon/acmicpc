#!/usr/bin/python3
import sys

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

preorder = []
idx = 0
def find_preorder(ino, posto):
#	global idx
#	print(str(idx) + " : ", end="")
#	idx += 1
#	print(preorder, end="")
	root = posto[-1]
	preorder.append(root)
	if len(ino[:ino.index(root)]) != 0:
		find_preorder(ino[:ino.index(root)], posto[:ino.index(root)])
	if len(ino[ino.index(root)+1:]) != 0:
		find_preorder(ino[ino.index(root)+1:], posto[ino.index(root):-1])

find_preorder(inorder, postorder)
print(*preorder)
