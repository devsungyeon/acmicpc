#!/bin/usr/python3
import sys

n, m = map(int, sys.stdin.readline().split());
trees = list(map(int, sys.stdin.readline().split()));

def calc(mid):
	global trees
	ret = 0
	for i in trees:
		ret += ((i-mid) if (i-mid) > 0 else 0)
	return ret

def cut(start, end, target):
	mid = (start + end) // 2
	chk = calc(mid)
	if (end-start) <= 1:
		return mid
	if chk >= target:
		return cut(mid, end, target)
	else:
		return cut(start, mid, target)
		
print(cut(0, max(trees), m))



