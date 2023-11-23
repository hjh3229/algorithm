N = int(input())
A = int(input())
L = [int(a) for a in str(A)]
sum = 0
for i in range(len(L)):
    sum += L[i]

print(sum)