import sys
a = list(sys.stdin.readline())
chk = "("
ans = 0
li = []
for i in a:
    if i == "(":
        li.append(1) 
    elif i == ")":
        if chk == "(":
            li.pop()
            for j in range(len(li)):
                li[j] += 1
        else:
            ans += li.pop()
    chk = i
print(ans)