import sys
input = sys.stdin.readline

while True:
    try:
        N = int(input())
        result = ["-"] * (3 ** N)
        n = 0
        for i in range(1, N + 1): # 전체 반복 횟수
            n = n * 3 + 1
            for j in range(n): # 지울 범위 갯수
                for k in range(3 ** (N - i)): # 지울 갯수
                    result[(3 ** (N - i)) * (2 * j + 1) + k] = " "
        ans = ''.join(result)
        print(ans)
    except :
        break


# def cantor_set(n):
#     if n == 0:
#         return '-'
#     prev_set = cantor_set(n - 1)
#     return prev_set + ' ' * len(prev_set) + prev_set
# while True:
#     try:
#         N = int(input())
#         print(cantor_set(N))
#     except EOFError:
#         break


# def cut(a,n):
#     if n == 1:
#         return
#     for i in range(a + n//3, a +(n//3)*2): 
#         result[i] = ' '
#     cut(a, n//3) 
#     cut(a + n//3 * 2, n//3) 
# import sys
# while True:
#     try :
#         N = int(sys.stdin.readline())
#         result = ['-']*(3**N) 
#         cut(0,3**N) 
#         print(''.join(result))
#     except :
#         break