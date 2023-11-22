N = int(input())
A = list(map(int, input().split()))
a = max(A)
ans = 0
for i in range(N):
    A[i] = (A[i] / a) * 100
    ans += A[i]

ans = ans / N
print(ans)