import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
nodes = {}
for i in range(1, n):
    nodes[i] = 0
edges = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u in edges:
        edges[u] += [v]
    else:
        edges[u] = [v]
answer = [0] * (n + 1)
order = 1
answer[r] = order

# for _ in range(n):
#     if r in edges:
#         for j in range(n):
#             if j in edges[r] and nodes[j] == 0:

