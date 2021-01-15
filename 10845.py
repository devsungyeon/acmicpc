import sys
queue = []
for _ in range(int(input())):
    li = list(map(str, sys.stdin.readline().split()))
    try:
        if li[0] == "push":
            queue.append(li[1])
        elif li[0] == "pop":
            print(queue.pop(0))
        elif li[0] == "size":
            print(len(queue))
        elif li[0] == "empty":
            if queue:   print(0)
            else:   print(1)
        elif li[0] == "front":
            print(queue[0])
        elif li[0] == "back":
            print(queue[-1])
    except:
        print(-1)