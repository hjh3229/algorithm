import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pok = []
for _ in range(N):
    pok.append(input().strip())

pok_dic1 = dict(zip(pok, list(range(1, len(pok) + 1))))
pok_dic2 = dict(zip(list(range(1, len(pok) + 1)), pok))

for _ in range(M):
    q = input().strip()
    if q.isdigit():
        print(pok_dic2[int(q)])
    else:
        print(pok_dic1[q])