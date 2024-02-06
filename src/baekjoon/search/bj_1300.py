N = int(input())
K = int(input())

start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N)
    
    if temp >= K:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)

# 아예 틀린 풀이였음...
# if K == 1:
#     print(1)
#     exit(0)
# elif K == N ** 2:
#     print(N ** 2)
#     exit(0)

# mid = (N * (N + 1)) // 2
# if K > mid:
#     ind = N ** 2 - K + 1
# else:
#     ind = K

# end = N
# stair = (end + 1) // 2
# while True:
#     cut = (stair * (stair + 1)) // 2
#     if ind > cut and ind <= cut + stair + 1:
#         break
#     if ind > cut:
#         stair = (stair + end) // 2
#     else:
#         end = stair
#         stair = (stair + 1) // 2

# if ind == K:
#     ind = (ind - cut + 1) // 2
#     print((stair - ind + 2) * ind)
# else:
#     ind = (ind - cut) // 2
#     a = (stair - ind) // 2
#     b = stair - a
#     print((N - a) * (N - b))