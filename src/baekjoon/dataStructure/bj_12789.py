import sys
input = sys.stdin.readline

N = int(input())
origin = list(map(int, input().split()))
sub = []

for i in range(1, N + 1):
    for _ in range(N):
        if origin[0] != i:
            if len(sub) != 0 and sub[-1] == i:
                sub.pop()
                break
            else:
                sub.append(origin.pop(0))
        else:
            origin.pop(0)
            break
        if len(origin) == 0:
            break
    if len(origin) == 0:
        break

for i in range(len(sub) - 1, -1, -1):
    origin.append(sub[i])

if sorted(sub) == origin:
    print("Nice")
else:
    print("Sad")