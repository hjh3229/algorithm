import sys
input = sys.stdin.readline

N = int(input())
stat_board = []
for _ in range(N):
    stat = list(map(int, input().split()))
    stat_board.append(stat)
min = 1e9

start = [1] * (N // 2)

def cal(last_member, index):
    global min
    if index == N // 2:
        start_synergy = 0
        link_synergy = 0
        link = []
        for i in range(2, N + 1):
            if not i in start:
                link.append(i)
        
        start_synergy = sum([stat_board[i-1][j-1] for i in start for j in start])
        link_synergy = sum([stat_board[i-1][j-1] for i in link for j in link])
        diff = abs(start_synergy - link_synergy)
        if diff == 0:
            print(0)
            exit(0)
        elif diff < min:
            min = diff
        return
    else:
        for i in range(last_member + 1, N + 1):
            start[index] = i
            cal(i, index + 1)

cal(1, 1)
print(min)