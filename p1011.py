import math
for i in range(int(input())):
    x, y = map(int,input().split())
    tmp = math.ceil(math.sqrt(y-x))*2-1
    if math.pow(math.ceil(math.sqrt(y-x)),2)-(y-x) < math.ceil(math.sqrt(y-x)):
        print(tmp)
    else:
        print(tmp-1)