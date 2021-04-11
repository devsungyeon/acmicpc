h, m = map(int, input().split())
if(m < 45):
    h += 23
    h %= 24
m += 15
m %= 60
print(str(h) + " " + str(m))