M, N = map(int, input().split())
banch = dict.fromkeys(range(1, M + 1), 1)
ans = [0] * N

def pair(index):
    if index == N:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, M + 1):
        if banch[i]:
            ans[index] = i
            banch[i] = 0
            pair(index + 1)
            banch[i] = 1

pair(0)