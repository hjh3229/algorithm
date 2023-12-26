import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

results = []
result = nums[0]

def cal(index):
    global result, a, b, c, d
    if index == N:
        results.append(result)
        return
    
    if a != 0:
        temp = result
        result += nums[index]
        a -= 1
        cal(index + 1)
        a += 1
        result = temp
    if b != 0:
        temp = result
        result -= nums[index]
        b -= 1
        cal(index + 1)
        b += 1
        result = temp
    if c != 0:
        temp = result
        result *= nums[index]
        c -= 1
        cal(index + 1)
        c += 1
        result = temp
    if d != 0:
        temp = result
        if result < 0:
            result = abs(result) // nums[index] * -1
        else:
            result //= nums[index]
        d -= 1
        cal(index + 1)
        d += 1
        result = temp

cal(1)

results.sort()
print(results[-1])
print(results[0])

# +, -, *, // 의 조합을 만드는 방법은 메모리 초과로 실패
# pmmd = ["+"] * a + ["-"] * b + ["*"] * c + ["//"] * d
# pmmd_list = list(itertools.permutations(pmmd))
# all_pmmd = []
# for i in pmmd_list:
#     all_pmmd.append(list(i))
# pmmds = [list(x) for x in set(tuple(x) for x in all_pmmd)]

# for i in range(len(pmmds)):
#     for j in range(len(pmmds[i])):
#         if pmmds[i][j] == "+":
#             result += nums[j + 1]
#         elif pmmds[i][j] == "-":
#             result -= nums[j + 1]
#         elif pmmds[i][j] == "*":
#             result *= nums[j + 1]
#         elif pmmds[i][j] == "//":
#             if result < 0:
#                 result = abs(result) // nums[j + 1] * -1
#             else:
#                 result //= nums[j + 1]
#     results.append(result)
#     result = nums[0]

# 딕셔너리를 사용한 방법도 시간초과로 실패 -> 백 트래킹 구조 자체를 다시 생각
# pmmd = {"+" : a, "-" : b, "*" : c, "/" : d}

# def cal(index):
#     global result, pmmd
#     if index == N:
#         results.append(result)
#         return
    
#     for i in range(N):
#         if pmmd["+"] != 0 and i <= a:
#             result += nums[index]
#             pmmd["+"] -= 1
#             cal(index + 1)
#             result -= nums[index]
#             pmmd["+"] += 1
#         elif pmmd["-"] != 0 and i <= a + b:
#             result -= nums[index]
#             pmmd["-"] -= 1
#             cal(index + 1)
#             result += nums[index]
#             pmmd["-"] += 1
#         elif pmmd["*"] != 0 and i <= a + b + c:
#             result *= nums[index]
#             pmmd["*"] -= 1
#             cal(index + 1)
#             result //= nums[index]
#             pmmd["*"] += 1
#         elif pmmd["/"] != 0 and i <= a + b + c + d:
#             temp = result
#             if result < 0:
#                 result = abs(result) // nums[index] * -1
#             else:
#                 result //= nums[index]
#             pmmd["/"] -= 1
#             cal(index + 1)
#             result = temp
#             pmmd["/"] += 1

# cal(1)