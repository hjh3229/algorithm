A = []
time = 0
sum = 0

for i in range(20):
    A.append(input().split())

for i in range(len(A)):
    if A[i][2] == "P":
        pass
    else:
        if A[i][2] == "A+":
            sum += float(A[i][1]) * 4.5
        elif A[i][2] == "A0":
            sum += float(A[i][1]) * 4.0
        elif A[i][2] == "B+":
            sum += float(A[i][1]) * 3.5
        elif A[i][2] == "B0":
            sum += float(A[i][1]) * 3.0
        elif A[i][2] == "C+":
            sum += float(A[i][1]) * 2.5
        elif A[i][2] == "C0":
            sum += float(A[i][1]) * 2.0
        elif A[i][2] == "D+":
            sum += float(A[i][1]) * 1.5
        elif A[i][2] == "D0":
            sum += float(A[i][1]) * 1.0
        elif A[i][2] == "F":
            sum += float(A[i][1]) * 0.0
        time += float(A[i][1])

print(round(sum / time, 6))        

# 아래 코드를 지향하자
# rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
# grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

# total = 0	
# result = 0	
# for _ in range(20) :
#     s, p, g = input().split()
#     p = float(p)
#     if g != 'P' :	
#         total += p
#         result += p * grade[rating.index(g)]

# print('%.6f' % (result / total))