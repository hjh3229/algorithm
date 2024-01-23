import sys

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))
white = 0
blue = 0

for i in range(N):
    for j in range(N):
        if paper[i][j] == 0:
            white += 1
        else:
            blue += 1

l = 2
while True:
    if l > N:
        break
    
    for i in range(N // l):
        for j in range(N // l):
            is_square = sum(sum(row[l * i:l * (i + 1)]) for row in paper[l * j:l * (j + 1)])
            if is_square == 0:
                white -= 3
            elif is_square == l ** 2:
                blue -= 3
    l *= 2

print(white)
print(blue)