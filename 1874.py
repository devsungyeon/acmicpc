import sys
def last_val(li):
    return li[len(li)-1]

n = int(input())

inputarr = [int(input()) for i in range(n)]

li = []
lipp = []

cnt = 1
for i in inputarr:
    for j in range(cnt, i+1):
        li.append(j)
        lipp.append("+")
        cnt += 1
    if i == last_val(li):            
        li.pop()
        lipp.append("-")
    else:
        print("NO")
        sys.exit()
for i in lipp:
    print(i)
    