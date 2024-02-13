import sys, heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    num = int(input())
    if num:
        hq.heappush(heap, (-num, num))
    else:
        if len(heap) > 0:
            print(hq.heappop(heap)[1])
        else:
            print(0)


# nums = [0]

# def compare(a):
#     global nums
#     start = 0
#     end = len(nums)
#     tmp = [0] * (end + 1)
#     while start < end:
#         mid = (start + end) // 2
#         if nums[mid] > a:
#             end = mid
#         else:
#             start = mid + 1
#     tmp[start] = a
#     for i in range(start):
#         tmp[i] = nums[i]
#     for i in range(start, len(nums)):
#         tmp[i + 1] = nums[i]
#     nums = tmp

# for _ in range(N):
#     num = int(input())
#     if num == 0:
#         if len(nums) == 1:
#             print(0)
#         else:
#             print(nums.pop())
#     else:
#         compare(num)