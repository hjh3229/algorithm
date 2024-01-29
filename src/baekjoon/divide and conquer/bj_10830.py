import sys
input = sys.stdin.readline

N, B = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

def multi(a, tmp):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * tmp[k][j]
                result[i][j] %= 1000
    return result

def divine(a, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    
    tmp = divine(a, b // 2)
    if b % 2 == 0:
        return multi(tmp, tmp)
    else:
        return multi(multi(tmp, tmp), a)

ans = divine(A, B)

for i in range(N):
    print(' '.join(map(str, ans[i])))