#!/usr/bin/python3

def bubblesort(x):
	for i in range(len(x)-1):
		for j in range(len(x) - i):
			if x[j] > x[j+1]:
				x[j], x[j+1] = x[j+1], x[j]
	return x
