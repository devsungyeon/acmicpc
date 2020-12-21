def VPS(li):
        if len(li) % 2 != 0 or li.count('(') != li.count(')'):
            return "NO"
        else:
            cnt = 0
            for j in li:
                if j == "(":
                    cnt -= 1
                else:
                    cnt += 1
                if cnt > 0:
                    return "NO"
            if cnt == 0:
                return "YES"
            return "NO"

for i in range(int(input())):
    li = list(str(input()))
    print(VPS(li))