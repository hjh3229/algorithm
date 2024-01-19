func_origin = list(input())

func = []
num = []             
for i in range(len(func_origin)):
    if func_origin[i] == '+' or func_origin[i] == '-':
        func.append(int(''.join(num)))
        num = []
        func.append(func_origin[i])
    elif i == len(func_origin) - 1:
        num.append(func_origin[i])
        func.append(int(''.join(num)))
    else:
        num.append(func_origin[i])

for i in range(len(func) - 1, 0, -1):
    if func[i] == '+':
        func[i - 1] = func[i - 1] + func[i + 1]
        func.pop(i)
        func.pop(i)

if len(func) > 1:
    for i in range(2, len(func), 2):
        func[0] -= func[i]
print(func[0])

# .split('+'), .split('-') 을 사용했다면 더 짧게 풀 수 있었을 것