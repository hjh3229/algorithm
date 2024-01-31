import sys
input = sys.stdin.readline

k, n  = map(int, input().split())
cables = []
for _ in range(k):
    cables.append(int(input()))

min_cable = 1
max_cable = max(cables)
current = (min_cable + max_cable) // 2

while min_cable <= max_cable:
    cnt = 0
    for cable in cables:
        cnt += cable // current
    if cnt >= n:
        min_cable = current + 1
        current = (min_cable + max_cable) // 2
    else:
        max_cable = current - 1
        current = (min_cable + max_cable) // 2

print(current)