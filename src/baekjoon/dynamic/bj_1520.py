# import sys
# input = sys.stdin.readline

# def go_left(row, col):
#     if col == 0:
#         return
    
#     if my_map[row][col] > my_map[row][col-1]:
#         my_way[row][col-1] += my_way[row][col]

# def go_right(row, col):
#     if col == M - 1:
#         return
    
#     if my_map[row][col] > my_map[row][col+1]:
#         my_way[row][col+1] += my_way[row][col]

# def go_up(row, col):
#     if row == N - 1:
#         return
    
#     if my_map[row][col] < my_map[row+1][col]:
#         my_way[row-1][col] += my_way[row][col]

# def go_down(row, col):
#     if row == N - 1:
#         return
    
#     if my_map[row][col] > my_map[row+1][col]:
#         my_way[row+1][col] += my_way[row][col]

# N, M = map(int, input().split())
# my_map = []
# for _ in range(N):
#     my_map.append(list(map(int, input().split())))

# my_way = [[0] * M for _ in range(N)]
# my_way[0][0] = 1
# my_way[N-1][M-1] = 1

# for i in range(N):
#     for j in range(M):
#         go_up(i, j)
#         go_left(i, j)
#         go_down(i, j)
#         go_right(i, j)

# print(my_way[N-1][M-1])
# print(my_way)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []

moves = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

visited = [[-1] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    for move in moves:
        nx, ny = x + move[0], y + move[1]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[x][y] < graph[nx][ny]:
                visited[x][y] += dfs(nx, ny)

    return visited[x][y]

print(dfs(n-1, m-1))