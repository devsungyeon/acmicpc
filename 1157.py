s = "baaa"
#s = input()
s = s.lower()
if len(s) > 1:
    li = [[chr(x), s.count(chr(x))] for x in range(97,123)]
    li.sort(key=lambda x:x[1], reverse=True)
    print("?" if (li[0][1] == li[1][1]) else li[0][0].upper())
else:
    print(s.upper())