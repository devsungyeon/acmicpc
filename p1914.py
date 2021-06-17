#!/usr/local/bin/python3
def Tn(k):
    return 2**k-1

def hanoi(k, s, m, d):
    if k<=0:
        return
    hanoi(k-1, s, d, m)
    print(str(s) + " " + str(d))
    hanoi(k-1, m, s, d)

n = int(input())
k = Tn(n)
print(k)
if k <= 20:
    hanoi(n, 1, 2, 3)