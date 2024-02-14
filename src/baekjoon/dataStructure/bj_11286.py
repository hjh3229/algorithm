import sys, heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    num = int(input())
    if num:
        if num > 0:
            hq.heappush(heap, (num, num))
        else:
            hq.heappush(heap, (-num - 0.1, num))
    else:
        if len(heap) > 0:
            print(hq.heappop(heap)[1])
        else:
            print(0)