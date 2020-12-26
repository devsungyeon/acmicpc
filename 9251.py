# import sys, itertools
# a = list(input())
# b = list(input())
# dp = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
# for i in range(1, len(b)+1):
#     for j in range(1, len(a)+1):
#         if a[j-1] == b[i-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# print(matrix[-1][-1])

import sys
s1 = sys.stdin.readline().strip().upper()
s2 = sys.stdin.readline().strip().upper()

len1 = len(s1)
len2 = len(s2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if s1[i-1] == s2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
print(matrix[-1][-1])