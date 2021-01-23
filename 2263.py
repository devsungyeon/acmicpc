#!/usr/bin/python3
import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
inloc = [0 for _ in range(n+1)]
for i in range(n):
	inloc[inorder[i]] = i
# inorder가 반드시 숫자 오름차순은 아니다!
preorder = []
idx = 0
def find_preorder(ins, ine, posts, poste):
	if posts <= poste:
		root = postorder[poste]
		print(root, end=" ")
		inrootidx = inloc[root]
		
		
		#find_preorder(ins, inrootidx-1, posts, posts+inrootidx-1-ins)
		#find_preorder(inrootidx+1, ine, poste-ine+inrootidx, poste-1)
	
		l_count=inrootidx-ins
		r_count=ine-inrootidx

		find_preorder(ins , ins+l_count-1 , posts, posts+l_count-1)
		find_preorder(ine-r_count+1, ine, poste-r_count, poste-1)
find_preorder(0, n-1, 0, n-1)
