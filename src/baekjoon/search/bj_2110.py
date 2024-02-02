import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()
# 기존에는 공유기를 설치하고 거리를 구했으나, 거리를 기준으로 목표한 수만큼 공유기를 설치하는 방법
start = 1 # 공유기 거리 최소
end = houses[-1] - houses[0] # 공유기 거리 최대
result = 0

# 재귀로 적절한 두 공유기 사이의 거리를 찾는다
while (start <= end):
    mid = (start + end) // 2 # 현재 공유기 거리
    current = houses[0]
    count = 1

    # 공유기 설치 몇 대 할 수 있는지 체크
    for i in range(1, len(houses)):
        if houses[i] >= current + mid:
            count += 1
            current = houses[i]
    # 공유기 설치 수가 목표 보다 크면 공유기 사이 거리 늘림
    if count >= C:
        start = mid + 1
        result = mid
    # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
    else:
        end = mid - 1

print(result)

# 이 방법은 너무 복잡하고 재귀가 너무 많이 일어나서 보류
# distance = [0] * (N - 1)
# for i in range(N - 1):
#     distance[i] = houses[i + 1] - houses[i]

# if C == 2:
#     print(houses[-1] - houses[0])
# elif C == N:
#     print(min(distance))
# else:
#     start = 0
#     end = N - 1
#     current = (end - start) // 2
#     point = 0
#     min_distance = 0
#     while not (current == start or current == end):
#         tmp = min(sum(distance[start:current]), sum(distance[current:end]))
#         if sum(distance[start:current]) > sum(distance[current:end]):
#             if tmp > min_distance:
#                 min_distance = tmp
#             start = current
#             current = (end - start) // 2
#         else:
#             end = current
#             current = (end - start) // 2
#     print(min_distance)