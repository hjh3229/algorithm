import sys, heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    num = int(input())
    if num:
        hq.heappush(heap, num)
    else:
        if len(heap) > 0:
            print(hq.heappop(heap))
        else:
            print(0)