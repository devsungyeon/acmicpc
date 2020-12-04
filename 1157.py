s = input()
s = s.lower()
ans = 0
ansout = ''
for i in range(97,123):
    tmp = s.count(chr(i))
    if tmp > ans:
        ans = tmp
        ansout = chr(i).upper()
    if tmp == ans:
        ansout = "?"

print(ansout)

