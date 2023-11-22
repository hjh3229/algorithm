N, M = map(int, input().split())
A = [0] * N
for a in range(M):
    i, j, k = map(int, input().split())
    for b in range(i-1, j):
        A[b] = k

print(*A)