import sys
input = sys.stdin.readline

w_array = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    global ans
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if w_array[a][b][c]:
        return w_array[a][b][c]
    elif a < b < c:
        w_array[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return w_array[a][b][c]
    else:
        w_array[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return w_array[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")

# 알고보니 중학생 때 푸는 최단경로 경우의 수 구하기 문제와 유사한 문제였다.