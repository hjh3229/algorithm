import sys

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(str, sys.stdin.readline().strip())))

l = 2
while True:
    if l > N:
        break
    
    ans = [[''] * (N // l) for _ in range(N // l)]
    for i in range(N // l):
        for j in range(N // l):
            prev = data[2*i][2*j] + data[2*i][2*j+1] + data[2*i+1][2*j] + data[2*i+1][2*j+1]
            if prev == '1111':
                ans[i][j] = '1'
            elif prev == '0000':
                ans[i][j] = '0'
            else:
                ans[i][j] = '(' + prev + ')'
    l *= 2
    copy = ans.copy()
    data = copy

print(data[0][0])