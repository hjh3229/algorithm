M, N = map(int, input().split())
ans = [0] * N

def pair(index):
    if index == N:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(1, M + 1):
        ans[index] = i
        pair(index + 1)

pair(0)