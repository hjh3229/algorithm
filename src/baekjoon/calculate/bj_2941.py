A = input()
croatia = ["c=", "c-", "dz=", "d-", "nj", "lj", "s=", "z="]

for i in croatia:
    A = A.replace(i, 'a')

print(len(A))