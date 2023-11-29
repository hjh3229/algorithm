n, m = map(int, input().split())
board = []
check = []
for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        sub_sum = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0 and board[x][y] == "B":
                    sub_sum += 1
                if (x + y) % 2 == 1 and board[x][y] == "W":
                    sub_sum += 1
        if sub_sum > 32:
            sub_sum = 64 - sub_sum
        check.append(sub_sum)

print(min(check))