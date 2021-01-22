#!/usr/bin/python3
import sys

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

preorder = []
idx = 1
def find_preorder(ino, posto):
	print(str(idx) + preorder)
	root = posto[-1]
	preorder.append(root)
	find_preorder(ino[:ino.index(root)], posto[:ino.index(root)])
	find_preorder(ino[ino.index(root)+1:], posto[:-1])

find_preorder(inorder, postorder)
