import sys
stack = []
for i in range(int(input())):
    li = list(map(str, sys.stdin.readline().split()))
    if li[0] == "push":
        stack.append(li[1])
    elif li[0] == "pop":
        print(stack.pop() if len(stack) != 0 else -1)
    elif li[0] == "size":
        print(len(stack))
    elif li[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif li[0] == "top":
        print(stack[len(stack)-1] if len(stack) != 0 else -1)