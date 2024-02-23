import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
orbs = list(map(int, input().split()))

dp = [0]
for weight in weights:
    tmp = []
    for i in dp:
        if i + weight in dp or i + weight in tmp:
            pass
        else:
            tmp.append(i + weight)
        if abs(i - weight) in dp or abs(i - weight) in tmp:
            pass
        else:
            tmp.append(abs(i - weight))
    dp = dp + tmp

for orb in orbs:
    if orb in dp:
        print("Y", end=" ")
    else:
        print("N", end=" ")


# 튜플을 이용하면 더 빠르다.
# import sys

# input = sys.stdin.readline

# N = int(input())
# grams = tuple(map(int, input().split()))
# K = int(input())
# check_grams = tuple(map(int, input().split()))

# d = {0}
# for gram in grams:
#     l = tuple(d)
#     for g in l:
#         d.add(abs(gram + g))
#         d.add(abs(gram - g))
#     d.add(gram)
# for gram in check_grams:
#     print("Y" if gram in d else "N", end=" ")