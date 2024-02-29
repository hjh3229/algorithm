import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
NGE= [-1]*N
my_stack = [0]

for i in range(1, N):
    while my_stack and A[my_stack[-1]] < A[i]:
        NGE[my_stack.pop()] = A[i]
    my_stack.append(i)
print(*NGE)

# 틀림
# my_stack.append(A.pop())
# answer = [-1]

# for _ in range(n-1):
#     my_stack.append(A.pop())
#     if my_stack[-1] < my_stack[-2]:
#         answer.append(my_stack[-2])
#     else:
#         if my_stack[-1] < answer[-1]:
#             answer.append(answer[-1])
#         else:
#             answer.append(-1)
# answer.reverse()
# print(*answer, sep=' ')

# 시간초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# answer = [0] * n
# A = list(map(int, input().split()))
# myStack = []

# for i in range(n):
#     while myStack and A[myStack[-1]] < A[i]:
#         answer[myStack.pop()] = A[i]
#     myStack.append(i)

# while myStack:
#     answer[myStack.pop()] = -1

# result = ""
# for i in range(n):
#     result += str(answer[i]) + " "

# print(result)