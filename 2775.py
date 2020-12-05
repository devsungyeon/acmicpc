# li = [[0]*15 for i in range(15)]
# for i in range(15): li[0][i] = i
# for i in range(1, 15):
#     for j in range(1,15):
#         li[i][j] = li[i-1][j] + li[i][j-1] 

# for i in range(int(input())):
#     k = int(input())
#     n = int(input())
#     print(li[k][n])


for i in range(int(input())):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]
    for __ in range(k):
        for j in range(1, n):
            people[j] += people[j-1] 
    print(people[-1])
#    print(li[k][n])
