import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    files = [0] + list(map(int, input().split()))

    sums = [0] * (K + 1)
    for i in range(1, K + 1):
        sums[i] = sums[i-1] + files[i]
    
    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]

    for i in range(2, K+1):
        for j in range(1, K+2-i):
            dp[j][j+i-1] = min([dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)]) + (sums[j+i-1] - sums[j-1])
    
    print(dp[1][K])

# pypy3으로 제출하면 통과. 다른 정답자들은 함수를 사용해 굉장히 빠르게 실행되는 프로그램을 제출했던데 정확한 원리는 모르겠음. 공부 필요
# def solution():
#     stdin = open(0, "rb")
#     T = int(stdin.readline())
#     for _ in range(T):
#         K = int(stdin.readline())
#         sizes = list(map(int, stdin.readline().split()))

#         ans = 0
#         cursor = 1
#         q = [1_000_000_000, sizes[0]] + [0] * K

#         def combine(end):
#             nonlocal ans
#             nonlocal cursor
#             cost = q[end-1] + q[end]
#             ans += cost

#             q.pop(end)
            
#             i = end-2
#             while q[i] < cost:
#                 i -= 1
#             q[i+2:end] = q[i+1:end-1]
#             q[i+1] = cost

#             cursor -= 1
#             while i > 0 and q[i-1] <= cost:
#                 d = cursor-i
#                 combine(i)
#                 i = cursor-d
#         ### enddef combine

#         for x in sizes[1:]:
#             while q[cursor-1] <= x:
#                 combine(cursor)
#             cursor += 1
#             q[cursor] = x
#         while cursor > 1:
#             combine(cursor)
#         print(ans)
# ### enddef solution

# solution()