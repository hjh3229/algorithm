import sys
input = sys.stdin.readline

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2 * i, 1000001, i):
            check[j] = 1

N = int(input())
for _ in range(N):
    q = int(input())
    cnt = 0
    for i in prime:
        if i >= q:
            break
        if not check[q - i] and i <= q - i:
            cnt += 1
    print(cnt)