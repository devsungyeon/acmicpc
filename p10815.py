n = int(input())
nli = list(map(int, input().split()))
nli.sort()
m = int(input())
mli = list(map(int, input().split()))


def binary_search(s, e, chk):
    ans = 0
    if s<=e:
        #print(s,e,chk)
        m = (s+e)//2
        #print("nli[m] : " + str(nli[m]))
        if nli[m] == chk:
            return 1
        elif nli[m] > chk:
            ans = binary_search(s, m-1, chk)
        else:
            ans = binary_search(m+1, e, chk)
    return ans

for i in mli:
    print(binary_search(0, n-1, i), end=" ")