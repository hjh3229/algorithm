N, K = map(int, input().split())
people = list(range(1, N + 1))

for i in range(N):
    target = (K - 1) % (N - i)
    people = people[:i] + people[target + i:] + people[i:target + i]

result = '<' + ', '.join(map(str, people)) + '>'
print(result)