n = int(input())
result = n
c = 0
while(1):
    c += 1
    a = n // 10
    b = n % 10
    n = b*10 + (a+b) % 10
    if(n == result):
        break
print(c)