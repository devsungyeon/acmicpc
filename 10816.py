import sys
n = int(sys.stdin.readline())
nli = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mli = list(map(int, sys.stdin.readline().split()))

tmp = {}
for i in nli:
    try:
        tmp[i] += 1
    except KeyError:
        tmp[i] = 1

for i in mli:
    try:
        print(tmp[i], end=' ')
    except KeyError:
        print(0, end=' ')