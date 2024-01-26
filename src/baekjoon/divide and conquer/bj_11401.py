n, k = map(int, input().split())
p = 1000000007

def factorial(N):
    a = 1
    for i in range(2, N + 1):
        a = (a * i) % p
    return a

def multi(N, K):
    if K == 1:
        return N
    elif K == 0:
        return 1
  
    tmp = multi(N, K // 2)
    if K % 2 == 0:
        return (tmp * tmp) % p
    else:
        return (tmp * tmp * N) % p

up = factorial(n)
down = factorial(n - k) * factorial(k) % p

ans = up * multi(down, p - 2) % p
print(ans)

# 파스칼 삼각형을 만드는 방법은 메모리 초과가 뜸
# pascal = [[0] * min(i, k + 1) for i in range(1, n + 2)]
# pascal[0][0] = 1
# for i in range(1, n + 1):
#     pascal[i][0] = 1
#     pascal[i][-1] = 1
#     p = min(i, k + 1)
#     for j in range(1, p):
#         pascal[i][j] = (pascal[i - 1][j] + pascal[i - 1][j - 1]) % 1000000007
#         if i == n and j == k:
#             print(pascal[i][j])
#             break

# 이항 계수의 원리를 이용한 함수는 재귀함수를 너무 많이 요청해서 보류
# def combi(a, b):
#     if a == b + 1 or b == 1:
#         return a
#     else:
#         return combi(a - 1, b) + combi(a - 1, b - 1)
    
# print(combi(n, k))