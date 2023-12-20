import sys
input = sys.stdin.readline

board = []
for _ in range(9):
    line = input().strip()
    board.append(list(map(int, line.split())))
blank =[]
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

def check_box(col, row, num):
    box_col = col // 3
    box_row = row // 3
    for i in range(3):
        for j in range(3):
            if num == board[3 * box_col + i][3 * box_row + j]:
                return False
    return True

def check_row(col, num):
    for i in range(9):
        if num == board[col][i]:
            return False
    return True

def check_col(row, num):
    for i in range(9):
        if num == board[i][row]:
            return False
    return True

def put_num(cnt):
    if cnt == len(blank):
        for i in range(9):
            print(*board[i])
        exit(0)
    
    col = blank[cnt][0]
    row = blank[cnt][1]
    for num in range(1, 10):
        if check_row(col, num) and check_col(row, num) and check_box(col, row, num):
            board[col][row] = num
            put_num(cnt + 1)
            board[col][row] = 0

put_num(0)


# 실패 사례
# check_num(col, row)
#     if board[col][row] == 0:
#         for i in range(1, 10):
#             if copy_board[col][row][i] == 0 and i == 9:
#                 return False
#             if copy_board[col][row][i]:
#                 board[col][row] = i
#             if row < 8:
#                 if put_num(col, row + 1):
#                     break
#             else:
#                 if col < 8:
#                     if put_num(col + 1, 0):
#                         break
#                 else:
#                     return True
#             return False
#     elif col == 8 and row == 8:
#         return False
#     else:
#         if row < 8:
#             put_num(col, row + 1)
#         else:
#             if col < 8:
#                 put_num(col + 1, 0)
#             else:
#                 return True