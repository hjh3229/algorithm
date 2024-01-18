A = [*input()]
B = [*input()]

dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])

# 더 빠른 방법
# import sys
# read = sys.stdin.readline

# word1, word2 = read().strip(), read().strip()
# l1, l2 = len(word1), len(word2)
# arr = [0] * l2

# for i in range(l1):
#     cnt=0
#     for j in range(l2):
#         if cnt < arr[j]:
#             cnt = arr[j]
#         elif word1[i] == word2[j]:
#             arr[j] = cnt + 1

# print(max(arr))

# 실패한 방법
# def find_lcs(s_index, l_index, i):
#     if s_index == min_len:
#         return
#     if l_index == len(longer):
#         return
    
#     for j in range(l_index, len(longer)):
#         if shorter[s_index] == longer[j]:
#             dp[i].append(shorter[s_index])
#             print(s_index, j)
#             find_lcs(s_index + 1, j + 1, i)
#             break
#     # find_lcs(s_index + 1, l_index, i)

# for i in range(min_len):
#     find_lcs(i, 0, i)

# max_length = max(len(word) for word in dp)
# index_of = max(range(len(dp)), key = lambda x: len(dp[x]))
# longest = dp[index_of]
# print(dp)