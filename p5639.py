def postorder(start, end):
    if start > end:
        return
    division = end + 1
    for i in range(start+1, end+1):
        if li[start] < li[i]:
            division = i
            break
    postorder(start+1,division-1)
    postorder(division,end)
    print(li[start])

import sys
sys.setrecursionlimit(10**9)
li = []
count = 0
while count <= 10000:
    try:
        num = int(sys.stdin.readline())
    except:
        break
    li.append(num)
    count += 1

postorder(0,len(li)-1)