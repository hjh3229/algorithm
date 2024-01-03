n = int(input())

root = {1:0}

def cal(n):
    if n in root.keys():
        return root[n]
    if n % 3 == 0:
        if n % 2 == 0:
            root[n] = min(cal(n // 3), cal(n // 2)) + 1
        else:
            root[n] = min(cal(n // 3), cal(n - 1)) + 1
    else:
        if n % 2 == 0:
            root[n] = min(cal(n // 2), cal(n - 1)) + 1
        else:
            root[n] = cal(n - 1) + 1
    return root[n]

print(cal(n))