n = int(input())

answer = 0

if n <= 99:
    answer = n
else:
    answer = 99
    for i in range(100,n+1):
        h = int(str(i)[0])
        t = int(str(i)[1])
        n = int(str(i)[2])
        if h-t == t-n:
            answer += 1

print(answer)