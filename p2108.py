import sys
import math
from collections import Counter
li = []
for i in range(int(input())):
    li.append(int(sys.stdin.readline()))
li.sort()

def mean(li):
    return round(sum(li)/len(li))

def median(li):
    return li[len(li)//2]

def mode(li):       
    mode_dict = Counter(li)
    modes = mode_dict.most_common()
    
    mod = modes[0][0]
    if len(modes) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
    return mod

def scope(li):
    return max(li)-min(li)

print(mean(li))
print(median(li))
print(mode(li))
print(scope(li))

# nums = sorted(nums)
# mode_dict = dict(zip(nums, [0]*len(nums)))

# for n in nums : 
#     mode_dict[n] += 1
    
# modes = [ k for k, v in mode_dict.items() if v == max(mode_dict.values())]