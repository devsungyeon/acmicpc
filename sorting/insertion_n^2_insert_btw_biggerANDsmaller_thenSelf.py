#!/usr/bin/python3
def insertionsort(x):
	for i in range(1, len(x)):
		j, key = i-1, x[i]
		while x[j] > key and j>=0:
			x[j+1] = x[j]
			j = j -1
		x[j+1] = key
	return x

