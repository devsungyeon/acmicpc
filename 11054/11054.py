#!/usr/bin/python3

n = int(input())
num_list = list(map(int, input().split()))
num_list_len = len(num_list)

maxval = num_list[n-1]

for i in range(0, int(num_list_len/2)):
	if ( num_list[i] + num_list[num_list_len-i-2]) > maxval :
		maxval = num_list[i] + num_list[num_list_len-i-2]

print(maxval)



