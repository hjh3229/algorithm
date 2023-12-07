import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

under_gcd = math.gcd(b, d)

ans_under = b * d // under_gcd
ans_on = a * d // under_gcd + c * b // under_gcd

check = math.gcd(ans_on, ans_under)

print(ans_on // check, ans_under // check)