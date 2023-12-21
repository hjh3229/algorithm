M, N = map(int, input().split())
ans = [0] * N

def pair(index, i):
    if index == N:
        print(' '.join(map(str, ans)))
        return
    for j in range(i + 1, M + 1):
        ans[index] = j
        pair(index + 1, j)

pair(0, 0)