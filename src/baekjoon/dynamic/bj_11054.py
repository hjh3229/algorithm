N = int(input())
A = list(map(int, input().split()))
A_reverse = []
for i in range(N - 1, -1, -1):
    A_reverse.append(A[i])
dp = [1] * N
dp_reverse = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        if A_reverse[i] > A_reverse[j]:
            dp_reverse[i] = max(dp_reverse[i], dp_reverse[j] + 1)

ans = [0] * N
for i in range(N):
    ans[i] = dp[i] + dp_reverse[N - i - 1] - 1

print(max(ans))