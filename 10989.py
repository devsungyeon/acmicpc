# import sys
# li = [0] * 10001
# for i in range(int(input())):
#     n = int(sys.stdin.readline())
#     li[n] += 1
# for i in range(10001):
#     if li[i] != 0:
#         for j in range(li[i]):
#             print(i)

import sys
N = int(input())

dic = {}

for i in range(N):
    a = int(sys.stdin.readline())

    if a in dic:
        dic[a] =  dic[a] +1

    else:
        dic[a] = 1
print(dic)
for q in sorted(dic.items()):
    for i in range(q[1]):
        print(q[0])