import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
set_A = sorted(list(set(A)))
C = dict(zip(set_A, list(range(len(set_A)))))

for i in A:
    print(C[i], end=" ")