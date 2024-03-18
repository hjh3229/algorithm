def dfs(t):
    global cnt
    visited[t] = cnt
    line[t].sort()
    for i in line[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

import sys
sys.setrecursionlimit(150000)
N, M, R = map(int, sys.stdin.readline().split())
line = [[] for _ in range(N+1)]
visited = [0]*(N+1)  # 저장값
cnt = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)  # 양 방향 간선
    line[b].append(a)  # 양 방향 간선
dfs(R)
for i in range(1, N+1):
    print(visited[i])
# 출처: https://edder773.tistory.com/71 [개발하는 차리의 공부 일기:티스토리]

# 컴파일 에러
# import sys
# input = sys.stdin.readline

# n, m, r = map(int, input().split())
# nodes = {}
# for i in range(1, n+1):
#     nodes[i] = 0 # 해당 노드 탐색 여부
# edges = {}
# for _ in range(m): # 간선 관계
#     u, v = map(int, input().split())
#     if u in edges:
#         edges[u] += [v]
#         if v in edges:
#             edges[v] += [u]
#         else:
#             edges[v] = [u]
#         edges[u].sort()
#     else:
#         edges[u] = [v]
#         if v in edges:
#             edges[v] += [u]
#         else:
#             edges[v] = [u]

# def dfs(prev_node):
#     global order
#     for node in edges[prev_node]:
#         if nodes[node] == 0:
#             order += 1
#             nodes[node] = order
#             dfs(node)

# order = 1
# nodes[r] = order
# dfs(r)

# for i in range(1, n+1):
#     print(nodes[i])
