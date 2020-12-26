import itertools

n = int(input())
li = [list(map(int, input().split())) for i in range(n)]

combination = list(itertools.combinations(range(n), int(n / 2)))
players = tuple(i for i in range(n))

def potential(pair):
    global li
    potential_val = 0
    pairs = list(set(itertools.permutations(pair, 2)))
    for i in pairs:
        potential_val += (li[i[0]][i[1]])
    return potential_val

ans = 100000000000

for i in combination:
    #(list(set(players) - set(i)))
    ans = min(ans, abs(potential(i) - potential(list(set(players) - set(i)))))
print(ans)