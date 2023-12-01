import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

for i in sorted(A):
    print(i)

# 간단하면서 현명한 답안
# import sys
# a = [False]*2_000_001
# for _ in range(int(input())):
#     a[int(sys.stdin.readline())] = True
# print('\n'.join(str(i) for i in range(-1_000_000, 1_000_001) if a[i]))