import sys
li = []
for i in range(int(input())):
    li.append(int(sys.stdin.readline()))
li.sort()
for i in li:
    print(i)