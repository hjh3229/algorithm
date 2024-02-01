import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()
distance = [0] * (N - 1)
for i in range(N - 1):
    distance[i] = houses[i + 1] - houses[i]

if C == 2:
    print(houses[-1] - houses[0])
elif C == N:
    print(min(distance))
else:
    start = 0
    end = N - 1
    current = (end - start) // 2
    min_distance = sum(distance)
    while True:
        tmp = min(sum(distance[start:current]), sum(distance[current:end]))
        if sum(distance[start:current]) > sum(distance[current:end]):
            start = current
            current = (end - start) // 2
        else:
            end = current
            current = (end - start) // 2
        if min_distance <= tmp:
            break
    