#!/bin/python3
a, b = map(int, input().split())
a = int(a/100) + int(a%100/10)*10 + a%10*100
b = int(b/100) + int(b%100/10)*10 + b%10*100
if a>b :
	print(a)
else:
	print(b)
