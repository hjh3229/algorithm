import sys

N = int(input())
A = {}
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    A[a] = b
keys = sorted(list(A.keys()))
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if A[keys[i]] > A[keys[j]]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))