import sys

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

m = 0
z = 0
p = 0

def check(row, col, n):
    global m, z, p
    curr = paper[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if paper[i][j] != curr:
                n //= 3
                check(row, col, n)  # 1
                check(row, col + n, n)  # 2
                check(row, col + (2 * n), n)  # 3
                check(row + n, col, n)  # 4
                check(row + n, col + n, n)  # 5
                check(row + n, col + (2 * n), n)  # 6
                check(row + (2 * n), col, n)  # 7
                check(row + (2 * n), col + n, n)  # 8
                check(row + (2 * n), col + (2 * n), n)  # 9
                return

    if curr == -1:
        m += 1
    elif curr == 0:
        z += 1
    elif curr == 1:
        p += 1
    return


check(0, 0, N)

print(m)
print(z)
print(p)

# 시간 초과
# 재귀 함수를 통해 범위 내에 다른 수가 있다면 최소 3*3까지 분할해서 각 원소를 확인
# def cut(row, col, len):
#     global m, z, p
#     if len == 1:
#         if paper[row][col] == -1:
#             m += 1
#         elif paper[row][col] == 0:
#             z += 1
#         elif paper[row][col] == 1:
#             p += 1
#         return
    
#     if len == 3:
#         check = paper[row][col]
#         square = [a[col:col+3] for a in paper[row:row+3]]
#         if not any(any(num != check for num in a) for a in square):
#             if check == -1:
#                 m += 1
#             elif check == 0:
#                 z += 1
#             elif check == 1:
#                 p += 1
#             return
#         else:
#             for i in range(3):
#                 for j in range(3):
#                     check = paper[row+i][col+j]
#                     if check == -1:
#                         m += 1
#                     elif check == 0:
#                         z += 1
#                     elif check == 1:
#                         p += 1
#             return
#     elif len > 3:
#         check = paper[row][col]
#         square = [a[col:col+len] for a in paper[row:row+len]]
#         if not any(any(num != check for num in a) for a in square):
#             if check == -1:
#                 m += 1
#             elif check == 0:
#                 z += 1
#             elif check == 1:
#                 p += 1
#             return
#         len //= 3
#         for i in range(len):
#             for j in range(len):
#                 cut(row + 3 * i, col + 3 * j, len)

# cut(0, 0 , N)
# print(m)
# print(z)
# print(p)