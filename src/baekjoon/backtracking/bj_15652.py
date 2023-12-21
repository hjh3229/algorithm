M, N = map(int, input().split())
ans = [0] * N

def pair(start, index):
    if index == N:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(start, M + 1):
        ans[index] = i
        pair(i, index + 1)

pair(1, 0)