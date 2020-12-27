import itertools
t = int(input())

def calc(li):
    ans = 1
    for i in li:
        ans *= li[i]
    return ans-1

for i in range(t):
    n = int(input())
    dic = {}
    for _ in range(n):
        clothName, clothkind = map(str, input().split())
        value = dic.get(clothkind)
        if value is None:
            dic[clothkind] = 2
        else:
            value += 1
            dic[clothkind] = value
    print(calc(dic))