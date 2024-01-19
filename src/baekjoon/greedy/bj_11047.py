import sys

N, K = map(int, input().split())
A = [0]
for _ in range(N):
    A.append(int(sys.stdin.readline()))

cnt = 0
def pay(target):
    global cnt
    if target == 0:
        print(cnt)
        exit(0)
    
    if target > 0:
        for i in range(N, 0, -1):
            if A[i] <= target:
                cnt += target // A[i]
                pay(target % A[i])

pay(K)