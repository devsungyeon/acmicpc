import sys
import math
n = sys.stdin.readline()
li = [int(sys.stdin.readline())]
li.append(int(sys.stdin.readline()))
gcd = abs(li[1]-li[0])
for i in range(2, int(n)):
    li.append(int(sys.stdin.readline()))
    gcd = math.gcd(gcd, abs(li[i]-li[i-1]))
gcd_a = int(gcd**0.5)
a = []
for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        a.append(i)
        a.append(gcd // i)
a.append(gcd)
a = list(set(a))
a.sort()
for i in a:
    print(i, end = ' ')