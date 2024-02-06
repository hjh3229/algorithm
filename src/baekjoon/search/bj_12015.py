import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

tmp = [A[0]]

def compare(a):
    start = 0
    end = len(tmp)

    while start <= end:
        mid = (start + end) // 2

        if tmp[mid] == a:
            return mid
        elif tmp[mid] > a:
            end = mid - 1
        else:
            start = mid + 1
        
    return start

for item in A:
    if tmp[-1] < item:
        tmp.append(item)
    else:
        idx = compare(item)
        tmp[idx] = item

print(len(tmp))