while True:
    A = int(input())
    if A == -1:
        break
    B = []
    for i in range(1, A // 2 + 1):
        if A % i == 0:
            B.append(i)
    if sum(B) == A:
        ans = f"{A} = "
        for j in range(len(B)):
            if j == len(B) - 1:
                ans += f"{B[j]}"
            else: 
                ans += f"{B[j]} + "
    else:
        ans = f"{A} is NOT perfect."
    print(ans)