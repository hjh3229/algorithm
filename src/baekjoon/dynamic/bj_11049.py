import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    r, c = map(int, input().split())
    matrix.append([r, c])

dp = [[[1, 1, 0] for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][i][0] = matrix[i-1][0]
    dp[i][i][1] = matrix[i-1][1]

for i in range(2, N + 1):
    for j in range(1, N + 2 - i):
        min_result = 2_147_483_648
        for k in range(i - 1):
            result = dp[j][j+i-k-2][0] * dp[j][j+i-k-2][1] * dp[j+i-k-1][j+i-1][1] + dp[j][j+i-k-2][2] + dp[j+i-k-1][j+i-1][2]
            if result < min_result:
                dp[j][j+i-1][2] = result
                dp[j][j+i-1][0] = dp[j][j+i-k-2][0]
                dp[j][j+i-1][1] = dp[j+i-k-1][j+i-1][1]
                min_result = result

print(dp[1][N][2])