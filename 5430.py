import sys
t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())
    li = list(map(str, sys.stdin.readline().split(',')))

    if li[0] == "[]\n":
        li.pop()
    else:
        li[0] = li[0][1:]
        li[-1] = li[-1][:-2]
    try:
        chk_reverse = 0
        for i in p:
            if i == "R":
                chk_reverse = not chk_reverse
            else:
                if chk_reverse: li.pop(-1)
                else:   li.pop(0)
        if chk_reverse: li.reverse()
        print('[' + ','.join(li) + ']')
    except AttributeError:
        print("error")
    except IndexError:
        print("error")