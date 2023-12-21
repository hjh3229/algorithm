import sys, itertools
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
pmmd = ["+"] * a + ["-"] * b + ["*"] * c + ["//"] * d
pmmd_list = list(itertools.permutations(pmmd))
all_pmmd = []
for i in pmmd_list:
    all_pmmd.append(list(i))
pmmds = [list(x) for x in set(tuple(x) for x in all_pmmd)]
results = []
result = nums[0]

for i in range(len(pmmds)):
    for j in range(len(pmmds[i])):
        if pmmds[i][j] == "+":
            result += nums[j + 1]
        elif pmmds[i][j] == "-":
            result -= nums[j + 1]
        elif pmmds[i][j] == "*":
            result *= nums[j + 1]
        elif pmmds[i][j] == "//":
            if result < 0:
                result = abs(result) // nums[j + 1] * -1
            else:
                result //= nums[j + 1]
    results.append(result)
    result = nums[0]

results.sort()
print(results[-1])
print(results[0])