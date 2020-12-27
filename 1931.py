import sys
n = int(sys.stdin.readline())
Is = []
for i in range(n):
    Is.append(list(map(int,sys.stdin.readline().split())))
Is.sort(key=lambda x: x[0])
Is.sort(key=lambda x: x[1])

last = 0
ans = 0
for i, j in Is:
    if i >= last:
        ans += 1
        last = j
print(ans)