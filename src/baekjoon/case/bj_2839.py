N = int(input())
a5 = 0
a3 = 0

for i in range(N // 3):
    a5 = (N // 5) - i
    if (N - (a5 * 5)) % 3 == 0:
        a3 = (N - (a5 * 5)) / 3
        print(int(a5 + a3))
        break

if 5 * a5 + 3 * a3 != N:
    print(-1)