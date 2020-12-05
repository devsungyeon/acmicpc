import math
a,b,v = map(int,input().split())
ans = int(math.ceil((v-a)/(a-b)))
print(ans+1)