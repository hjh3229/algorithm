import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
lst_req = list(map(int, input().split()))

lst.sort()
cnt = {}
for i in lst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in lst_req:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')

# N = int(input())
# cards = sorted([*map(int, input().split())])
# M = int(input())
# candidate = [*map(int, input().split())]

# count = {}
# for card in cards:
#     if card in count:
#         count[card] += 1
#     else:
#         count[card] = 1

# def binarySearch(arr, target, start, end):
#     if start > end:
#         return 0
    
#     mid = (start + end) // 2
#     if arr[mid] == target:
#         return count.get(target)
#     elif arr[mid] < target:
#         return binarySearch(arr, target, mid+1, end)
#     else:
#         return binarySearch(arr, target, start, mid-1)
    
# for target in candidate:
#     print(binarySearch(cards, target, 0, len(cards)-1), end=" ")