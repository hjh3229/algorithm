N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min = price[0]
ans = distance[0] * min
for i in range(1, N - 1):
    if price[i] < min:
        min = price[i]
    ans += distance[i] * min

print(ans)