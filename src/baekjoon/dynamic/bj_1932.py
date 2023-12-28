import sys

N = int(input())
tri = []
for _ in range(N):
    tri.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(len(tri[i])):
        if j == len(tri[i]) - 1:
            tri[i][j] += tri[i - 1][j - 1]
        elif j == 0:
            tri[i][j] += tri[i - 1][0]
        else:
            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

print(max(tri[N - 1]))