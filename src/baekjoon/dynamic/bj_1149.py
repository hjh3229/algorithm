import sys

N = int(input())
rgb_cost = []
for _ in range(N):
    rgb_cost.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(3):
        rgb_cost[i][j] += min(rgb_cost[i - 1][j - 1],rgb_cost[i - 1][j - 2])

print(min(rgb_cost[N - 1]))