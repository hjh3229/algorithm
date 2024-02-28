my_string = list(input().strip())
bomb = list(input().strip())
bomb_len = len(bomb)
my_stack = []

for s in my_string:
    my_stack.append(s)
    if my_stack[len(my_stack)-bomb_len:len(my_stack)] == bomb:
        for _ in range(bomb_len):
            my_stack.pop()

if len(my_stack) == 0:
    print("FRULA")
else:
    print(*my_stack, sep='')

# 더 빠름
# sample_str = input()
# str_bomb = list(input())
# answer = []

# for i in sample_str:
#     answer.append(i)
#     if i == str_bomb[-1] and answer[len(answer) - len(str_bomb):] == str_bomb:
#         for _ in str_bomb:
#             answer.pop()

# if answer:
#     print(''.join(map(str, answer)))
# else:
#     print('FRULA')

# 시간초과
# while bomb in my_string:
#     tmp = ''
#     banch = ''
#     for i in range(len(my_string)):
#         if (len(banch) == 0 and my_string[i] == bomb[0]) or (len(banch) != 0 and my_string[i] != bomb[0]):
#             banch += my_string[i]
#             if len(banch) == len(bomb):
#                 if banch != bomb:
#                     tmp += banch
#                 banch = ''
#         else:
#             tmp += my_string[i]
#     my_string = tmp

# if len(my_string) == 0:
#     print("FRULA")
# else:
#     print(my_string)