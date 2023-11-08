import sys
input = sys.stdin.readline
3
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
temp = [0] * (N+1)
result = 0

def merge_sort(s, e):
    global result
    if e-s < 1: return
    m = int(s+(e-s) / 2)
    merge_sort(s, m)
    merge_sort(m+1, e)
    for i in range(s, e+1):
        temp[i] = A[i]
    
    k = s
    index1 = s
    index2 = m+1
    while index1 <= m and index2 <= e:
        if temp[index1] > temp[index2]:
            A[k] = temp[index2]
            result = result + index2 - k
            k += 1
            index2 += 1
        else:
            A[k] = temp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = temp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = temp[index2]
        k += 1
        index2 += 1

merge_sort(1, N)
print(result)