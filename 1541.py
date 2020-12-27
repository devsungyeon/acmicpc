func = list(input())
li = []
li.append(0)
for i in func:
    if i != '+' and i != '-':
        li[-1] = int(li[-1]) * 10 +int(i)
    else:
        li.append(i)
        li.append(0)
while(True):
    try:
        idx = li.index('+')
        b = li.pop(idx+1)
        li.pop(idx)
        a = li.pop(idx-1)
        li.insert(idx-1, a+b)
    except ValueError:
        break
ans = li[0]
for i in li[1:]:
    if i != '-':
        ans -= i

print(ans)