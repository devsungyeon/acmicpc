import math
n = int(input())
print(int(n/5)+int(n/25)+int(n/125))
def last(q):
    ans = 0
    if q == 0:
        return 0
    while(True):
        if q%10 == 0:
            ans += 1
        else:
            break
        q = q//10
    return ans

for i in range(0, 501):
    print(str(i) + ": " + str(last(math.factorial(i))) +" " + str(math.factorial(i)))