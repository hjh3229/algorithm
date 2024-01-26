import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

ans = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            ans[i][j] += A[i][k] * B[k][j]
    print(' '.join(map(str, ans[i])))