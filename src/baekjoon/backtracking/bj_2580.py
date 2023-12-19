board = []
copy_board = []
for _ in range(9):
    line = input().strip()
    board.append(list(map(int, line.split())))
    copy_board.append(list(map(int, line.split())))

def check_box(col, row, num):
    box = []
    box_col = col // 3
    box_row = row // 3
    for i in range(3):
        for j in range(3):
            box.append(board[3 * box_col + i][3 * box_row + j])
    if num in box:
        return True
    return False

def check_num(col, row):
    if board[col][row] == 0:
        nums = {1 : 1, 2 : 1, 3 : 1, 4 : 1, 5 : 1, 6 : 1, 7 : 1, 8 : 1, 9 : 1}
        for i in range(9):
            if i + 1 in board[col]:
                nums[i + 1] = 0
            if check_box(col, row, i + 1):
                nums[i + 1] = 0
            for j in range(9):
                if board[j][row] == i + 1:
                    nums[i + 1] = 0
        copy_board[col][row] = nums

def put_num(col, row):
    check_num(col, row)
    if board[col][row] == 0:
        for i in range(1, 10):
            if copy_board[col][row][i] == 0 and i == 9:
                return False
            if copy_board[col][row][i]:
                board[col][row] = i
            if row < 8:
                if put_num(col, row + 1):
                    break
            else:
                if col < 8:
                    if put_num(col + 1, 0):
                        break
                else:
                    return True
    elif col == 8 and row == 8:
        return True
    else:
        if row < 8:
            put_num(col, row + 1)
        else:
            if col < 8:
                put_num(col + 1, 0)
            else:
                return True

put_num(0, 0)

for row in board:
    print(' '.join(map(str, row)))