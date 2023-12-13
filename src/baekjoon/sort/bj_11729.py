def front(a):
    front = a
    front = front.replace('2', 'x').replace('3', '2').replace('x', '3')
    return front

def behind(a):
    behind = a
    behind = behind.replace('1', 'x').replace('2', '1').replace('x', '2')
    return behind

N = int(input())

ans = "1 3"

for i in range(N - 1):
    ans = front(ans) + "1 3" + behind(ans)

print(2 ** N - 1)
for i in range(0, len(ans), 3):
    print(ans[i:i + 3])

# def hanoi_tower(n, source, auxiliary, target):
#     if n == 1:
#         print(source, target)
#     else:
#         hanoi_tower(n - 1, source, target, auxiliary)
#         print(source, target)
#         hanoi_tower(n - 1, auxiliary, source, target)

# N = int(input())
# total_moves = 2**N - 1
# print(total_moves)

# hanoi_tower(N, 1, 2, 3)