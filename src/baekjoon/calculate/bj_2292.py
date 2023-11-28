A = int(input())
B = (A - 1) / 6
check = 0
ans = 0
for i in range(A):
    if A == 1:
        ans = 1
        break
    check += i
    if check >= B:
        ans = i + 1
        break

print(ans)

# a=int(input())
# b=1
# c=0
# while True:
#     if a>b:
#         c+=1
#         b+=(c*6)
#     else:
#         print(c+1)
#         break