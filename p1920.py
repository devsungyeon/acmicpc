import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline())
mli = list(map(int, sys.stdin.readline().split()))

for i in mli:
    try:
        a.index(i)
        print(1)
    except ValueError:
        print(0)
