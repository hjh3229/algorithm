import sys

N, K = map(int, input().split())
items = [[0, 0]]
for _ in range(N):
    items.append(list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = items[i][0]
        value = items[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[N][K])

# 더 빠른 방법
# n, k = map(int, input().split())
# dp = [0] * (k+1)
# for _ in range(n):
#     w, v = map(int, input().split())
#     if w > k:
#         continue
#     for i in range(k, 0, -1):
#         if i + w <= k and dp[i] != 0:
#             dp[i+w] = max(dp[i+w], dp[i]+v)
#     dp[w] = max(dp[w], v)

# print(max(dp))

# 실패 케이스 2
# for i in range(1, N + 1):
#     weight[0][i] = items[i - 1][0]
#     value[0][i] = items[i - 1][1]

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if i == j:
#             weight[i][j] = weight[0][j]
#             value[i][j] = value[0][j]
#         else:
#             if weight[i - 1][j] + items[i - 1][0] <= K:
#                 weight[i][j] = weight[i - 1][j] + items[i - 1][0]
#                 value[i][j] = value[i - 1][j] + items[i - 1][1]
#             else:
#                 weight[i][j] = weight[i - 1][j]
#                 value[i][j] = value[i - 1][j]

# max_row = [max(row) for row in value]
# print(max(max_row))

# 실패 케이스 1
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if i != j:
#             if weight[i][j - 1] + items[j - 1][0] > K:
#                 if value[i][j - 1] > value[i - 1][j]:
#                     value[i][j] = value[i][j - 1]
#                     weight[i][j] = weight[i][j - 1]
#                 else:
#                     value[i][j] = value[i - 1][j]
#                     weight[i][j] = weight[i - 1][j]
#             else:
#                 if value[i][j - 1] > value[i - 1][j]:
#                     value[i][j] = value[i][j - 1] + items[j - 1][1]
#                     weight[i][j] = weight[i][j - 1] + items[j - 1][0]
#                 else:
#                     value[i][j] = value[i - 1][j] + items[j - 1][1]
#                     weight[i][j] = weight[i - 1][j] + items[j - 1][0]
#         else:
#             value[i][j] = value[i][j - 1]
#             weight[i][j] = value[i][j - 1]
# print(weight, value)
# print(max(value[N][N - 1], value[N - 1][N]))