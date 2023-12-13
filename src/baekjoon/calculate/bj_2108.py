import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
nums_counter = {}

aver = round(sum(nums) / N)
mid = nums[(N + 1) // 2 - 1]
for num in nums:
    if num in nums_counter:
        nums_counter[num] += 1
    else:
        nums_counter[num] = 1
max_mode = max(nums_counter.values())
mode_banch = []
for num in nums_counter.keys():
    if nums_counter[num] == max_mode:
        mode_banch.append(num)
if len(sorted(mode_banch)) > 1:
    mode = mode_banch[1]
else:
    mode = mode_banch[0]
range = nums[N - 1] - nums[0]

print(aver)
print(mid)
print(mode)
print(range)
# 최빈값 실패 함수
# mode = nums[0]
# cnt = 1
# fre = 1
# mode_banch = []
# for i in range(N - 1):
#     if nums[i] == nums[i + 1]:
#         cnt += 1
#     if nums[i] != nums[i + 1] or i == N - 2:
#         if cnt == fre:
#             cnt = 1
#             mode_banch.append(nums[i])
#             if fre == 1:
#                 mode_banch.append(nums[i + 1])
#         elif cnt > fre:
#             mode_banch.clear()
#             fre = cnt
#             cnt = 1
#             mode = nums[i]
#             mode_banch.append(nums[i])
# if len(mode_banch) > 1:
#     mode = sorted(mode_banch)[1]