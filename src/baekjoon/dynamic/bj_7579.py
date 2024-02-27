# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# memory = [0] + list(map(int, input().split()))
# cost = [0] + list(map(int, input().split()))
# dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(n + 1)]
# min_cost = sum(cost)

# for i in range(1, n + 1):
#     m1 = memory[i]
#     c = cost[i]
#     if c == 0:
#         m -= m1
#         pass
#     for j in range(1, sum(cost) + 1):
#         if j < c:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(m1 + dp[i-1][j-c], dp[i-1][j])

#         if dp[i][j] >= m:
#             min_cost = min(min_cost, j)

# if m != 0:
#     print(min_cost)
# else:
#     print(0)

import sys

N, M = map(int, sys.stdin.readline().split())
m = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
c_max = sum(c)

dp = [0 for _ in range(c_max + 1)]

for i in range(N):
	for j in range(c_max, -1, -1):
		if(j < c[i]):
			continue
		if(dp[j] < dp[j - c[i]] + m[i]):
			dp[j] = dp[j - c[i]] + m[i]

for i in range(c_max + 1):
	if(dp[i] >= M):
		print(i)
		break