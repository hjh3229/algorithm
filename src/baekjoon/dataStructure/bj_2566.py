A = []
max = 0
x = 0
y = 0

for i in range(9):
    A = list(map(int, input().split()))
    for j in range(9):
        if A[j] >= max:
            max = A[j]
            x = j + 1
            y = i + 1

print(max)
print(y, x)