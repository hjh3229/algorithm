A = str(input())
L = [str(a) for a in str(A)]
t = 0
for i in range(len(L)):
    if ord(L[i]) < 68:
        t += 3
    elif ord(L[i]) < 71:
        t += 4
    elif ord(L[i]) < 74:
        t += 5
    elif ord(L[i]) < 77:
        t += 6
    elif ord(L[i]) < 80:
        t += 7
    elif ord(L[i]) < 84:
        t += 8
    elif ord(L[i]) < 87:
        t += 9
    elif ord(L[i]) < 91:
        t += 10
print(t)