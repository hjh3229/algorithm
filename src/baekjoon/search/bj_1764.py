import sys
input = sys.stdin.readline

N, M = map(int, input().split())
not_lis = []
for _ in range(N):
    not_lis.append(input().strip())

lis_list = dict(zip(not_lis, [1] * N))

is_seen_lis = []
for _ in range(M):
    is_seen = input().strip()
    if lis_list.get(is_seen, 0):
        is_seen_lis.append(is_seen)

is_seen_lis.sort()

print(len(is_seen_lis))
for i in is_seen_lis:
    print(i)