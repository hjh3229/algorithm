import sys
input = sys.stdin.readline

n = int(input())
answer = [0] * n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:
        answer[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    answer[myStack.pop()] = -1

result = ""
for i in range(n):
    result += str(answer[i]) + " "

print(result)