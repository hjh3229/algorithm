import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

min_height = min(trees)
max_height = max(trees)
if min_height == max_height:
    min_height = 0
current = (min_height + max_height) // 2

while min_height <= max_height:
    len = 0
    for tree in trees:
        if tree > current:
            len += tree - current
    
    if len >= M:
        min_height = current + 1
        current = (min_height + max_height) // 2
    else:
        max_height = current - 1
        current = (min_height + max_height) // 2

print(current)