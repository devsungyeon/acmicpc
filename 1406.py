from sys import stdin

stk1 = list(stdin.readline().split())
stk2 = []
n = int(input())
for _ in range(n):
    line = list(stdin.readline().split())
    if line[0] == 'L':
        if stk1:    stk2.append(stk1.pop())
        else:   continue
    elif line[0] == 'D':
        if stk2:    stk1.append(stk2.pop())
        else:   continue
    elif line[0] == 'B':
        if stk1:    stk1.pop()
        else:   continue
    elif line[0] == 'P':
        stk1.append(line[1])
print(''.join(stk1+list(reversed(stk2))))
