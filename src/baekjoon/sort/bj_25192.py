import sys
input = sys.stdin.readline

N = int(input())
hello = set()
cnt = 0
for _ in range(N):
    user = input().strip()
    if user == "ENTER":
        cnt += len(hello)
        hello.clear()
    else:
        hello.add(user)
cnt += len(hello)
print(cnt)