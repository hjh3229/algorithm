import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
F = {}
for a in A:
    if a in F:
        F[a] += 1
    else:
        F[a] = 1

answer = [-1] * n
my_stack = [0]

for i in range(1, n):
    while my_stack and F[A[my_stack[-1]]] < F[A[i]]:
        answer[my_stack.pop()] = A[i]
    my_stack.append(i)

print(*answer)