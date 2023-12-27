import sys

N = int(input())
length = [0] * 101
length[1] = 1
length[2] = 1
length[3] = 1

for _ in range(N):
    T = int(sys.stdin.readline())
    for i in range(4, T + 1):
        length[i] = length[i - 2] + length[i - 3]
    
    print(length[T])