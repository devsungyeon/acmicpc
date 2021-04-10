import sys
n, s = sys.stdin.readline().split()
li = {}
for i in range(int(n)):
    nickname, ans = sys.stdin.readline().split()
    li[nickname] = ans
cnt = 0
for i in li:
    if i == s:
        break
    if li[i] == li[s]:
        cnt += 1
print(cnt)