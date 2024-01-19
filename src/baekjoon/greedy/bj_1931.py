import sys

N = int(input())
sch = []
for _ in range(N):
    sch.append(list(map(int, sys.stdin.readline().split())))
sch.sort()

time = sch[-1][0]
cnt = 1
for i in range(N - 2, -1, -1):
    if sch[i][1] <= time:
        time = sch[i][0]
        cnt += 1

print(cnt)