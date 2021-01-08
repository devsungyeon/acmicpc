import sys

a,b,c = map(int, sys.stdin.readline().split())
binaryb = []
while b != 0:
    binaryb.append(b % 2)
    b = b // 2
binaryb.reverse()

ans = 1
for i in binaryb:
    ans = (ans**2*pow(a,i))%c
print(ans)