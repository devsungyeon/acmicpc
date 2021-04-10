import sys, math
n = sys.stdin.readline()
li = list(map(int, sys.stdin.readline().split()))
for i in li[1:]:
    print(str(int(li[0]/math.gcd(li[0],i))) + "/" + str(int(i/math.gcd(li[0],i))))